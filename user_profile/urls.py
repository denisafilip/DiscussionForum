from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.user_register, name="Register"),
    path("login/", views.user_login, name="Login"),
    path("logout/", views.user_logout, name="Logout"),
    path("myprofile/", views.my_profile, name="Myprofile"),
]
