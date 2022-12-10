from rest_framework.views import APIView
from .serializers import UserSerializer,ProductSerializer,ProductCategorySerializer
from rest_framework.response import Response
from rest_framework import generics, mixins
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from .models import CustomUser,Product,ProductCategory
import jwt
import datetime


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


class ProductsView(mixins.ListModelMixin, mixins.CreateModelMixin,
                generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

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



class ProductsCategoryView(mixins.ListModelMixin, mixins.CreateModelMixin,
                generics.GenericAPIView):

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

    def delete(self, request, *args, **kwargs):
        if not is_authenticated(request):
            raise AuthenticationFailed('Unauthenticated')

        obj_id = kwargs.pop('pk')
        obj = self.queryset.filter(id=obj_id).first()

       

        return self.destroy(request, *args, **kwargs)
