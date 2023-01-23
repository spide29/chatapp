from re import template
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('signup', views.signup, name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('reset_password', auth_views.PasswordResetView.as_view(template_name="authentication/password_reset.html"), name="reset_password"),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="authentication/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="authentication/password_reset_done.html"), name="password_reset_complete"),



    # Reset Password
    #path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    #path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    #path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    #path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]