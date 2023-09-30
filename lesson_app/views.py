from django.db.models import Sum
from .models import Product, ProductAccess, Lesson, LessonView, LessonUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import LessonViewSerializer
from django.contrib.auth import get_user



class LessonListView(APIView):
    def get(self, request):
        user = self.request.user.id
        user_lessons = LessonView.objects.filter(user=user)
        serializer = LessonViewSerializer(user_lessons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class ProductLessonListView(APIView):
    def get(self, request, product_id):
        user = get_user(request)
        product = get_object_or_404(Product, id=product_id)

        if not ProductAccess.objects.filter(product_id=product_id, user_id=user.id).exists():
            return Response({"message": "У вас нет доступа к этому продукту."}, status=status.HTTP_403_FORBIDDEN)

        lessons = product.lessons.all()
        lesson_views = LessonView.objects.filter(user=user, lesson__in=lessons).order_by('-id')
        lesson_views_serializer = LessonViewSerializer(lesson_views, many=True)
        last_lesson = lesson_views.last()
        last_lesson_serializer = LessonViewSerializer(last_lesson)

        lesson_data = []
        lesson_data.append({
            "last_lesson": last_lesson_serializer.data,
            "lessons": lesson_views_serializer.data,
        })

        return Response(lesson_data, status=status.HTTP_200_OK)



class ProductStatsView(APIView):
    def get(self, request):
        products = Product.objects.all()
        total_users = LessonUser.objects.count()

        product_stats = []
        for product in products:
            lesson_views = LessonView.objects.filter(lesson__products=product, is_viewed=True)

            time_spent = 0
            for lesson_view in lesson_views:
                time_spent += lesson_view.lesson.duration_seconds

            students_count = ProductAccess.objects.filter(product_id=product).count()

            purchase_percentage = (ProductAccess.objects.filter(product_id=product).count() / total_users) * 100

            product_stat = {
                "product_id": product.id,
                "product_name": product.title,
                "lesson_views": lesson_views.count(),
                "time_spent": time_spent,
                "students_count": students_count,
                "purchase_percentage": purchase_percentage,
            }

            product_stats.append(product_stat)
        return Response(product_stats, status=status.HTTP_200_OK)

