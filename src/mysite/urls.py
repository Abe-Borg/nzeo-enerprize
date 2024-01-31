"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . views import create_account, error_page, change_password, change_email, redirect_after_login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-account/', create_account, name='create_account'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'forgot_password.html'), name = 'password_reset'),
    path('', auth_views.LoginView.as_view(template_name = 'enerprize_home_page.html'), name = 'login'),
    path('redirect_after_login/', redirect_after_login, name = 'redirect_after_login'),
    path('district-management/', include('district_management.urls')),
    path('documents/', include('documents.urls')),
    # path('enerprize-api/', include('enerprize_api.urls')),
    path('maps/', include('maps.urls')),
    path('nzeo-management/', include('nzeo_management.urls')),
    path('school-management/', include('school_management.urls')),
    path('error_page/', error_page, name='error_page'),
    path('change_password/', change_password, name='change_password'),
    path('change_email/', change_email, name='change_email'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)