from rest_framework import serializers
from .models import Product, Lesson, Group

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'video_link']

class ProductSerializer(serializers.ModelSerializer):
    lessons_count = serializers.IntegerField(source='lessons.count', read_only=True)
    author = serializers.StringRelatedField()
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'author', 'title', 'start_date', 'price', 'lessons_count', 'lessons']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']