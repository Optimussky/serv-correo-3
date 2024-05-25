from django.db import models
from django.contrib.auth.models import User
#import uuid

class Notification(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    uuid = models.CharField(max_length=250)
    body = models.TextField()
    email = models.EmailField(unique=True)
    title = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')


