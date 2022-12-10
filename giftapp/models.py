from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid
from djmoney.models.fields import MoneyField


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password) 
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class CustomUser(AbstractUser):
    uniqueID = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=100)
    username = 'username'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_username(self):
        return self.email

class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    rank = models.IntegerField()
    product_category =models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        
    )
    created_time = models.DateTimeField(auto_now_add=True, editable=False)
    updated_time = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return str(self.name)

class Wishlist(models.Model):
    user =models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
        
    )
    wish =models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        
    )

    def __str__(self):
        return str(self.wish)

    def add_product_to_wishlist(self,wish):
        product_category = Product.Objects.get(id=wish)
        user = self.user_id
        
        wishlists = Wishlist.objects.filter(user=user, product__product_category_id=product_category.id)
        if not wishlists: 
            Wishlist.objects.create(user=user, product_id=wish)
        else:
            return 


    