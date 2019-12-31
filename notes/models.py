from django.db import models
from uuid import uuid4

from django.contrib.auth.models import User
# Create your models here.
# inherits from models.Model
class Note(models.Model):
    #  will be fields in databse
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)

class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)