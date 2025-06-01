from django.db import models

# Create your models here.
# inquiry/models.py
class Inquiry(models.Model):
    name        = models.CharField(max_length=50)
    email       = models.EmailField()
    phone       = models.CharField(max_length=20, blank=True)
    message     = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)