from django.db import models

class MyModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()