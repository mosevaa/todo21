from user.apps import UserConfig

APP_NAME = UserConfig.name

class PAGES:
    LOGIN = f"{APP_NAME}:login"

class TEMPLATES:
    LOGIN = f"{APP_NAME}/login.html"
    