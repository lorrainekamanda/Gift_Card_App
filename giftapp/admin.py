from django.contrib import admin
from .models import CustomUser,Product,ProductCategory,Wishlist

# Register your models here.

class WishlistAdmin(admin.ModelAdmin):
    # regular stuff
    USE_DJANGO_JQUERY = True
    class Media:
       js = ('https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js',
    'js/bindfield.js','js/chainedfk.js')
admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Wishlist,WishlistAdmin)