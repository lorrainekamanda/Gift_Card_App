from rest_framework import serializers
from .models import CustomUser,Product,ProductCategory,Wishlist
from rest_framework_money_field import MoneyField
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.conf import settings
from smart_selects.form_fields import ChainedModelChoiceField
from drf_extra_fields.relations import PresentablePrimaryKeyRelatedField

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser

        fields = [

            'id','email', 'password'
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance

class ProductSerializer(serializers.ModelSerializer):
    
    category_name = serializers.ReadOnlyField(source='product_category.name')
    class Meta:
        model = Product
        
        fields = [

            'id','name','price','price_currency','rank','category_name','product_category',
            'created_time'
        ]

        extra_kwargs = {
           
            'product_category': {'write_only': True},
        
        }


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory

        fields = [

            'id','name'
        ]


class WishListSerializer(serializers.ModelSerializer):
   
    user = serializers.ReadOnlyField(source='user.email')
    category = serializers.ReadOnlyField(source='category.name')
   
    

    class Meta:
    
        model = Wishlist
        
        fields = ['user','category','wish']



    
class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128)
    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)

    set_password_form_class = SetPasswordForm

    def __init__(self, *args, **kwargs):
        self.old_password_field_enabled = getattr(
            settings, "OLD_PASSWORD_FIELD_ENABLED", False
        )
        self.logout_on_password_change = getattr(
            settings, "LOGOUT_ON_PASSWORD_CHANGE", False
        )
        super(PasswordChangeSerializer, self).__init__(*args, **kwargs)

        if not self.old_password_field_enabled:
            self.fields.pop("old_password")

        self.request = self.context.get("request")
        self.user = getattr(self.request, "user", None)

    def validate_old_password(self, value):
        invalid_password_conditions = (
            self.old_password_field_enabled,
            self.user,
            not self.user.check_password(value),
        )

        if all(invalid_password_conditions):
            err_msg = _(
                "Your old password was entered incorrectly. Please enter it again."
            )
            raise serializers.ValidationError(err_msg)
        return value

    def validate(self, attrs):
        self.set_password_form = self.set_password_form_class(
            user=self.user, data=attrs
        )

        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)
        return attrs

    def save(self):
        self.set_password_form.save()
        if not self.logout_on_password_change:
            from django.contrib.auth import update_session_auth_hash

            update_session_auth_hash(self.request, self.user)
