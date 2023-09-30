from django.contrib import admin
from .models import LessonUser, Lesson, LessonView, ProductAccess, Product

# Register your models here.

admin.site.register(LessonUser)
admin.site.register(Lesson)
admin.site.register(LessonView)
admin.site.register(Product)
admin.site.register(ProductAccess)

