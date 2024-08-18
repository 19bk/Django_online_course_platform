from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    video_link = models.URLField()

    def __str__(self):
        return f"{self.product.title} - {self.title}"

class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='groups')
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.product.title} - {self.name}"

class StudentGroup(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('student', 'group')