from django.db import models
from django.contrib.auth.models import User
from shop.models import Product


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100,)
    email = models.EmailField(max_length=100,)
    address1 = models.CharField(max_length=100,)
    address2 = models.CharField(max_length=100,)
    city = models.CharField(max_length=100,)
    state = models.CharField(max_length=100, null=True, blank=True)
    zip = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100,)

    def __str__(self):
        return f'Shipping Address: {str(self.id)}'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100,)
    email = models.EmailField(max_length=100,)
    shipping_address = models.TextField(max_length=500)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    date_ordered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Order: {str(self.id)}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True,)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True,)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Order Item: {str(self.id)}'
