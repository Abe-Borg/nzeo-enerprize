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
from . import views
from django.contrib.auth.views import LoginView
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name = 'enerprize_home_page.html'), name = 'login'),
    # path('test-base-minimal/', views.test_base_minimal, name = 'test_base_minimal'),
    # path('test-base-nav-top-sidebar/', views.test_base_nav_top_sidebar, name = 'test_base_nav_top_sidebar'),
    # path('test-base-side-navbar/', views.test_base_side_navbar, name = 'test_base_side_navbar'),
    # path('test-base-top-navbar/', views.test_base_top_navbar, name = 'test_base_top_navbar'),
    # path('test-account-settings/', views.test_account_settings, name = 'test_account_settings'),
    # path('test-create-account/', views.test_create_account, name = 'test_create_account'),
    # path('test-forgot-password/', views.test_forgot_password, name = 'test_forgot_password'),
    path('district-management/', include('district_management.urls')),
    path('documents/', include('documents.urls')),
    path('enerprize-api/', include('enerprize_api.urls')),
    path('maps/', include('maps.urls')),
    path('nzeo-management/', include('nzeo_management.urls')),
    path('school-management/', include('school_management.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)