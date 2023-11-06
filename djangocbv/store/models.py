from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(_("name"),max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(_('name'),max_length=255)
    description = models.TextField(_('description'),)
    price = models.DecimalField(_('price'),max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='category_products',verbose_name=_('category'))
    image = models.ImageField(_('image'),upload_to='product_images/', null=True, blank=True)  # Add this line for the image field
    
    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, verbose_name=_("customer"), on_delete=models.CASCADE,null=True)
    name = models.CharField(_('name'),max_length=200)
    email = models.EmailField(_('email'),unique=True)
    address = models.TextField(_('address'),)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,verbose_name=_('customer'),null=True)
    products = models.ManyToManyField(Product, through='OrderItem')
    order_date = models.DateTimeField(auto_now_add=True,verbose_name=_('order_date'),null=True)
    total_price = models.DecimalField(_('total_price'),max_digits=10, decimal_places=2, validators=[MinValueValidator(0)],null=True)
    is_confirmed = models.BooleanField(_("is confirmed"),null=True)
    def __str__(self):
        return f"Order #{self.id} - {self.customer.name}"

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name=_('product'))
    order = models.ForeignKey(Order, on_delete=models.CASCADE,verbose_name=_('order'))
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)],verbose_name=_('quantity'))
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order #{self.order.id}"



class Setting(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE,related_name='user_settings',null=True)
    key = models.CharField(_("key"), max_length=50)
    value = models.CharField(_("value"), max_length=50)
    def __str__(self):
        return self.key
