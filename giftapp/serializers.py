from rest_framework import serializers
from .models import CustomUser,Product,ProductCategory


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

    class Meta:
        model = Product

        fields = [

            'id', 'price', 'rank', 'product_category',
            'created_time', 'updated_time', 'author_name'
        ]


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory

        fields = [

            'id','name'
        ]