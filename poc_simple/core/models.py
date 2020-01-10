import uuid
from django.db import models


class BaseModel(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tool(BaseModel):

    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.IntegerField()
