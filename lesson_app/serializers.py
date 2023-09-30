from rest_framework import serializers
from .models import LessonUser, Lesson, LessonView, Product



class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=10)


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    owner = serializers.PrimaryKeyRelatedField(queryset=LessonUser.objects.all())


class ProductAccessSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=LessonUser.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())


class LessonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    video_link = serializers.URLField()
    duration_seconds = serializers.IntegerField()
    products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


class LessonViewSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField()
    lesson_id = serializers.IntegerField()
    view_time = serializers.DateTimeField()
    is_viewed = serializers.BooleanField()

