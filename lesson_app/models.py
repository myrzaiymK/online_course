from django.db import models


class LessonUser(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.username


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(LessonUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ProductAccess(models.Model):
    user_id = models.ForeignKey(LessonUser, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_id.username} -> {self.product_id.title}"


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    video_link = models.URLField()
    duration_seconds = models.PositiveIntegerField()
    products = models.ManyToManyField(Product, related_name='lessons')

    def __str__(self):
        return self.title


class LessonView(models.Model):
    user = models.ForeignKey(LessonUser, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    view_time = models.DateTimeField()
    is_viewed = models.BooleanField()

    def __str__(self):
        return f"{self.user.username} viewed {self.lesson.title}"

