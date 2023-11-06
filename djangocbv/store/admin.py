from django.contrib import admin
from store import models

admin.site.register(models.Category)
admin.site.register(models.Customer)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.Setting)

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True