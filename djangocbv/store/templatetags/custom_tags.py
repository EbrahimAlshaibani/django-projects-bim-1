from django import template
from store.models import *
from django.db.models import Sum
register = template.Library()

@register.simple_tag
def theme():
    theme = Setting.objects.get(key="theme")
    return theme.value

@register.simple_tag
def totalBill(user):
    customer = Customer.objects.get(user=user)
    order = Order.objects.filter(customer=customer).last()
    total_price = 0.0
    if order is not None:
        total_price = order.total_price
    return total_price

@register.simple_tag
def totalCart(user):
    customer = Customer.objects.get(user=user)
    order = Order.objects.filter(customer=customer).last()
    orders = order.orderitem_set.all()
    total_orders = orders.aggregate(Sum('quantity'))
    total = 0.0
    if order is not None:
        total = total_orders['quantity__sum']
    return total