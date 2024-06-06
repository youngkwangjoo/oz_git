from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", views.Users.as_view()), # api/v1/users
    path("myinfo", views.MyInfo.as_view()),
    path("getToken", obtain_auth_token),
]