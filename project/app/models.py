from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField()
    bio=models.TextField()
    id=models.AutoField()

