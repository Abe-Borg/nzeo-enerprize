# account/urls.py

from django.urls import path, include
from django.contrib.auth.views import ( 
    LogoutView, 
    PasswordChangeView, 
    PasswordResetView, 
    PasswordResetConfirmView, 
    PasswordResetDoneView, 
    PasswordResetCompleteView, 
    PasswordChangeDoneView 
)
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('registration/', include('registration.backends.default.urls'), name = 'register'),
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page='enerprize_home'), name='logout'),
    path('must_authenticate/', views.must_authenticate_view, name='must_authenticate'),
    path('password_change/', PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    
    path('password_reset/', PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
