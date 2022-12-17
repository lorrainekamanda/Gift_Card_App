from rest_framework.views import APIView
from .serializers import UserSerializer,ProductSerializer,ProductCategorySerializer,WishListSerializer,PasswordChangeSerializer
from rest_framework.response import Response
from rest_framework import generics, mixins,response
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from .models import CustomUser,Product,ProductCategory,Wishlist
import jwt
import datetime
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
import django_filters
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator
from rest_framework.renderers import TemplateHTMLRenderer
from collections import OrderedDict


class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class LoginView(APIView):

    def post(self, request):
        email = request.data.get("email", "")
        password = request.data.get("password", "")

        user = CustomUser.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
        response.set_cookie('jwt', token, httponly=True)

        response.data = {
            'token': token,
            'email': user.email
        }

        return response



def is_authenticated(request, *args, **kwargs):
    token = request.COOKIES.get('jwt')
    if not token:
        return False
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        user = CustomUser.objects.filter(id=payload.get('id')).first()
        request.user = user

    except jwt.ExpiredSignatureError:
        return False

    return True

def is_permission_allowed(request, obj, *args, **kwargs):
    return obj.user == request.user
    
class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'price': ['lt', 'gt'],
           
        }

class ProductsView(mixins.ListModelMixin, mixins.CreateModelMixin,
                generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = (DjangoFilterBackend,OrderingFilter)
    filterset_class = ProductFilter
    ordering_fields = ('rank','created_time')
    
    

    def get(self, request, *args, **kwargs):
       
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not is_authenticated(request):
            raise AuthenticationFailed('Unauthenticated')

        return self.create(request, *args, **kwargs)



class ProductView(mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               generics.GenericAPIView):

    """ get,delete and update a product """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        if not is_authenticated(request):
            raise AuthenticationFailed('Unauthenticated')

        obj_id = kwargs.pop('pk')
        obj = self.queryset.filter(id=obj_id).first()

      
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if not is_authenticated(request):
            raise AuthenticationFailed('Unauthenticated')

        obj_id = kwargs.pop('pk')
        obj = self.queryset.filter(id=obj_id).first()

       

        return self.destroy(request, *args, **kwargs)



class ProductsCategoryView(mixins.ListModelMixin, 
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    
    """ get,delete and post a Product Category """

    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

    def get(self, request, *args, **kwargs):
       
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not is_authenticated(request):
            raise AuthenticationFailed('Unauthenticated')

        return self.create(request, *args, **kwargs)



class ProductCategoryView(mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               generics.GenericAPIView):

    """ get and delete a productCategory """

    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

    def get(self, request, *args, **kwargs):
        
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        
        if not is_authenticated(request):
            raise AuthenticationFailed('Unauthenticated')

        
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if not is_authenticated(request):
            raise AuthenticationFailed('Unauthenticated')

        obj_id = kwargs.pop('pk')
        obj = self.queryset.filter(id=obj_id).first()

       

        return self.destroy(request, *args, **kwargs)




class WishlistsView(mixins.ListModelMixin, mixins.CreateModelMixin,
                generics.GenericAPIView):
    """
    Add Wishlist Product Per category.
    """

    def get_queryset(self):
            user = self.request.user

            return Wishlist.objects.filter(user_id=user)

    
    serializer_class = WishListSerializer

    def get(self, request, *args, **kwargs):
        
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not is_authenticated(request):
            raise AuthenticationFailed('Unauthenticated')
        return self.create(request, *args, **kwargs)
        
     
class WishlistView(mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               generics.GenericAPIView):

    """ get and delete a Wishlist"""

    queryset = Wishlist.objects.all()
    serializer_class = WishListSerializer

    def get(self, request, *args, **kwargs):
        
        return self.retrieve(request, *args, **kwargs)
 
    

    def delete(self, request, *args, **kwargs):
        if not is_authenticated(request):
            raise AuthenticationFailed('Unauthenticated')

        obj_id = kwargs.pop('pk')
        obj = self.queryset.filter(id=obj_id).first()

        if obj and not is_permission_allowed(request, obj):
            raise PermissionDenied()

        return self.destroy(request, *args, **kwargs)

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters(
        "password", "old_password", "new_password1", "new_password2"
    )
)

class PasswordChangeView(generics.GenericAPIView):
    """
    Update the existing password with new one.
    Accepts the following POST parameters: new_password1, new_password2
    Returns the success/fail message.
    """

    serializer_class = PasswordChangeSerializer
    permission_classes = (IsAuthenticated,)

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(PasswordChangeView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response({"detail": ("New password has been saved.")})