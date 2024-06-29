from django.db import models

# Create your models here.
class Conversation(models.Model):
    summary=models.TextField(null=True,blank=True)
