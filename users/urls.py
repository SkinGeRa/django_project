from django.urls import path

from users.apps import UsersConfig
from users.views import verification_user, success_verification, set_new_password, RegisterView, LoginView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verification/', verification_user, name='verification'),
    path('success_verification/', success_verification, name='success_verification'),
    path('reset_password/', set_new_password, name='reset_password'),
]