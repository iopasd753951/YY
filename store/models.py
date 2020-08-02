import uuid
from django.db import models

from taggit.managers import TaggableManager
from taggit.models import TagBase, TaggedItemBase


class Store(models.Model):
    store_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    store_name = models.CharField(max_length=255)
    store_content = models.TextField()
    store_tag = TaggableManager()
    created_at = models.DateTimeField(auto_now=True)
