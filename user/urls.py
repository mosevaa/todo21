from django.urls import path

from user.views import UserLoginView

app_name = "user"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
]