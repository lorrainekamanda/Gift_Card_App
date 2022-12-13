from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from djmoney.models.fields import MoneyField
from babel.numbers import list_currencies
from smart_selects.db_fields import ChainedForeignKey
CURRENCY_CHOICES = [(currency, currency) for currency in list_currencies()] 


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
    price = models.CharField(max_length=14)
    price_currency = models.CharField(
        max_length=3, default='USD', choices=CURRENCY_CHOICES
    ) 
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
    category =models.OneToOneField(
        ProductCategory,
        on_delete=models.CASCADE,
        
    )
    wish = ChainedForeignKey(
        Product,
        chained_field="category",
        chained_model_field="name",
        
        auto_choose=True,
        sort=True,
        
        
    )

    def __str__(self):
        return str(self.wish)


   

  


    