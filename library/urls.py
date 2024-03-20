"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("book/", include("bookinstance.urls")),
    re_path(r'^api-auth/', include('rest_framework.urls')),
    re_path(r"^api/v1/books/", include('bookinstance.urls')),
    path('account/', include('django.contrib.auth.urls')),
]

# ba in reavesh mitone ye url baray login kardan tarif koni be form osoli tar
# va baray in ke bad az login be safhe admin nare bayad dastor zir ro toy setting.py gharar bedi
# LOGIN-REDIRECT_URL = '/'

# 'django.contrib.auth.urls'
# Addresses added here :

# accounts/login
# accounts/logout
# accounts/password_change
# accounts/password_change_done
# accounts/password_reset
# accounts/password_reset/done
# accounts/reset/<uidb64>/token/ [name = 'password_reset_confirm']
# accounts/reset/done