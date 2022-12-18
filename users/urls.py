from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.UserSignupView.as_view(), name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('exit/', views.exit, name='exit'),
    path('profile/', views.profile, name='profile'),
    path('pass-reset/', views.PassResetView.as_view(), name='pass-reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name='users/password-reset-done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', views.PassResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name='users/password-reset-complete.html'), name='password_reset_complete'),
]
