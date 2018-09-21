from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns = [

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='custom_registration/password_reset_form.html'),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='custom_registration/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='custom_registration/password_reset_confirm.html')
         , name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='custom_registration/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password_change/',
         auth_views.PasswordChangeView.as_view(template_name='custom_registration/password_change_form.html'),
         name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeView.as_view(template_name='custom_registration/password_change_done.html'),
         name='password_change_done'),


]
