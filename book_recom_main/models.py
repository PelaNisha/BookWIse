from django.db import models
from django.utils import timezone

# Create your models here.
class user_data(models.Model):
    u_name =  models.CharField(max_length=100, default="None")
    book_name =  models.CharField(max_length=200, default="None")
    author = models.CharField(max_length=200, default="None")
    book_id = models.IntegerField(primary_key = True, default=0)
    created_at = models.DateTimeField(default=timezone.now)


class Book(models.Model):
    ISBN = models.CharField(max_length=13, unique=True, default=123)
    Book_Title = models.CharField(max_length=255)
    Book_Author = models.CharField(max_length=255)
    Year_Of_Publication = models.IntegerField()
    Publisher = models.CharField(max_length=255)
    Image_URL_S = models.URLField()
    Image_URL_M = models.URLField()
    Image_URL_L = models.URLField()

    def __str__(self):
        return self.Book_Title
        
class Rating(models.Model):
    User_ID = models.IntegerField()
    ISBN = models.CharField(max_length=13)
    Book_Rating = models.IntegerField()

    def __str__(self):
        return f"User {self.User_ID} rated ISBN {self.ISBN} with {self.Book_Rating}"

class User(models.Model):
    User_ID = models.IntegerField(primary_key=True)
    Location = models.CharField(max_length=255)
    Age = models.IntegerField()

    def __str__(self):
        return f"User {self.User_ID}"

