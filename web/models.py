
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class PostModel(models.Model):
    title = models.CharField(max_length=100)
    beschreibung = models.TextField(max_length=1000)
    preis = models.CharField(max_length=5)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(PostModel, self).delete(*args, **kwargs)
