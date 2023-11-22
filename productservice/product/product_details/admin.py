from django.contrib import admin
from .models import products, purchase

admin.site.register(products)
admin.site.register(purchase)