from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count
from django.shortcuts import get_object_or_404
from .models import Product, Group
from users.models import UserBalance, ProductAccess
from .serializers import ProductSerializer, GroupSerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['post'])
    def pay(self, request, pk=None):
        product = self.get_object()
        user = request.user
        
        if not user.is_authenticated:
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)
        
        user_balance = get_object_or_404(UserBalance, user=user)
        
        if user_balance.amount < product.price:
            return Response({"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)
        
        user_balance.amount -= product.price
        user_balance.save()
        
        ProductAccess.objects.create(user=user, product=product)
        
        return Response({"message": "Payment successful. Access granted."}, status=status.HTTP_200_OK)

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    @action(detail=True, methods=['get'])
    def students(self, request, pk=None):
        group = self.get_object()
        students = group.studentgroup_set.all().select_related('student')
        data = [{"id": s.student.id, "username": s.student.username} for s in students]
        return Response(data)