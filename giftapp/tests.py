from django.test import TestCase
from rest_framework.test import APIRequestFactory,APITestCase,APIClient
from django.contrib.auth import get_user_model
from .models import Product,ProductCategory,Wishlist
User = get_user_model()



class CustomUserTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@test.ru', password='testpass123')
        self.admin_user = User.objects.create_superuser(email='superadmin@mail.com',password='testpass1234')

    def test_create_user(self):
        self.assertEqual(self.user.email, 'test@test.ru')
        self.assertFalse(self.user.is_superuser)
  

    def test_create_superuser(self):
        self.assertEqual(self.admin_user.email, 'superadmin@mail.com')
        self.assertTrue(self.admin_user.is_superuser)


class LoginTests(TestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(email='test@test.ru', password='pass1234')
        self.user.username = self.user.email
        self.user.save()

    def test_correct_login(self):
        self.assertTrue(self.client.login(email='test@test.ru', password='pass1234'))
        self.client.logout()

    def test_wrong_username(self):
        self.assertFalse(self.client.login(email='wrong', password='pass1234'))

    def test_wrong_pssword(self):
        self.assertFalse(self.client.login(email='test@test.ru', password='wrong'))



class TestSignup(APITestCase):
    def test_signup(request):

        client = APIClient()
        client.post('/api/sign-up/', {'email': 'test@gmail.com','password':"test1234"}, format='json')
        client.login(email='test@gmail.com', password='test1234')

    def tearDown(self) -> None:
        return super().tearDown()

class TestProductCategory(APITestCase):
    def test_productcategory(request):

        factory = APIRequestFactory()
        request = factory.post('/api/category-view/', {'name': 'New Year'}, format='json')
        request = factory.get('/api/category-view/', {'name': 'New Year'}, format='json')
        request = factory.delete('/api/category-view/', {'name': 'New Year'}, format='json')
        

    def tearDown(self) -> None:
        return super().tearDown()


class TestProduct(APITestCase):
    def test_product(request):

        factory = APIRequestFactory()
        request = factory.post('/api/products-view/', {'name': 'car','price':'5000','price_currency': 'USD',
                                'rank':5,'category':"new year"}, format='json')
        
        request = factory.get('/api/products-view/', {'name': 'car','price':'5000','price_currency': 'USD',
                                'rank':5,'category':"new year"}, format='json')

        request = factory.delete('/api/products-view/', {'name': 'car','price':'5000','price_currency': 'USD',
                                'rank':5,'category':"new year"}, format='json')
        

    def tearDown(self) -> None:
        return super().tearDown()


