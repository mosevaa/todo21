from django.db.models import (
    Model,
    CharField,
    TextField,
    DateTimeField,
    ForeignKey,
    CASCADE,
    SET_NULL,
    TextChoices
)

from user.models import User
from project.models import Project


class Task(Model):
    class TaskStatus(TextChoices):
        NEW = "NEW"
        PROCESSING = "PROCESSING"
        DONE = "DONE"

    name = CharField(max_length=50, null=False)
    description = TextField(null=True)
    project = ForeignKey(Project, on_delete=CASCADE)
    created_by = ForeignKey(User, on_delete=SET_NULL, null=True, related_name="creator")
    created_at = DateTimeField(null=False, auto_now_add=True)
    performer = ForeignKey(User, on_delete=SET_NULL, null=True, related_name="performer")
    status = CharField(max_length=15, choices=TaskStatus.choices, default=TaskStatus.NEW)
