from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Discount)
admin.site.register(ProductCategory)
admin.site.register(ProductImages)