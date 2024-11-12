from django.db.models import (
    Model,
    CharField,
    TextField,
    DateTimeField,
    ForeignKey,
    CASCADE
)
from user.models import User

class Project(Model):
    name = CharField(max_length=50, null=False)
    description = TextField(null=True)
    created_at = DateTimeField(null=False, auto_now_add=True)
    created_by = ForeignKey(User, on_delete=CASCADE)