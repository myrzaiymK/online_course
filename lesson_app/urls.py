from rest_framework.urls import path
from .views import LessonListView, ProductLessonListView, ProductStatsView

urlpatterns = [
    path('lesson_list_view/', LessonListView.as_view()),
    path('product_lesson_list/<int:product_id>/', ProductLessonListView.as_view()),
    path('product_stats/', ProductStatsView.as_view()),
]
