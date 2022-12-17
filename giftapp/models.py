from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
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
    user_id =models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
        
    )
  
    product_id= models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='product'
    
        
    )

    def __str__(self):
        return '{}'.format(self.product_id)


    @property
    def email(self):
        return self.user_id.email
    
    @property
    def id(self):
        return self.id
    @property
    def product(self):
        return self.product_id.name

    @property
    def category(self):
        return self.product_id.product_category.name

    def save(self, *args, **kwargs):
        
        user = self.user_id
        wishlists = Wishlist.objects.filter(user_id=user,product_id__product_category=self.product_id.product_category)
        if not wishlists:
            super(Wishlist, self).save(*args, **kwargs)
        else:
            return
        
        


   

  


    