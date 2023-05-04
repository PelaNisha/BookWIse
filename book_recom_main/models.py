from django.db import models
from django.utils import timezone
# Create your models here.
class user_data(models.Model):
    u_name =  models.CharField(max_length=100, default="None")
    book_name =  models.CharField(max_length=200, default="None")
    author = models.CharField(max_length=200, default="None")
    book_id = models.IntegerField(primary_key = True, default=0)
    created_at = models.DateTimeField(default=timezone.now)