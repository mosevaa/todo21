from typing import Any
from django.contrib.auth.forms import AuthenticationForm

class UserAuthForm(AuthenticationForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(UserAuthForm, self).__init__(*args, **kwargs)
        