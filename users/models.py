from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

User = get_user_model()

class UserBalance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='balance')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=1000, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.user.username} - Balance: {self.amount}"

class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_accesses')
    product = models.ForeignKey('courses.Product', on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"