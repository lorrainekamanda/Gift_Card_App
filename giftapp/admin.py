from django.contrib import admin
from .models import CustomUser,Product,ProductCategory,Wishlist

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Wishlist)