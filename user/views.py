from django.contrib.auth.views import LoginView

from user.constants import TEMPLATES
from user import forms

class UserLoginView(LoginView):
    http_method_names = ["get", "post"]
    form_class = forms.UserAuthForm
    template_name = TEMPLATES.LOGIN
