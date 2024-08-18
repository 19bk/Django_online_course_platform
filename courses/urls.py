from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, GroupViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'groups', GroupViewSet, basename='group')

urlpatterns = [
    path('', include(router.urls)),
]