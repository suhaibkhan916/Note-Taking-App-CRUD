from django.db import models
import uuid


class Notes(models.Model):
    table_id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    note_title = models.CharField(max_length=255)
    content_field = models.TextField(null=True)

    def __str__(self):
        return str(self.note_title)
