from django.contrib import admin

# Register your models here.
from .models import Time
from .models import Product

admin.site.register(Product)


admin.site.register(Time)
