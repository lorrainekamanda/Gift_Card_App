"""giftprojects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_swagger.views import get_swagger_view
from .yasg import urlpatterns as doc_urls
from django.views.generic.base import TemplateView


schema_view = get_swagger_view(title='Wishlist Api')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('giftapp.urls')),
    path('chaining/', include('smart_selects.urls')),
    path('api/docs/', schema_view),
    path('sw.js', TemplateView.as_view(template_name="sw.js", 
    content_type='application/javascript'), name='sw.js'),
    
]
