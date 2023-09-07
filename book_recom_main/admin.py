from django.contrib import admin

from book_recom_main.models import user_data, Book, User, Rating
admin.site.register(user_data)
admin.site.register(Book)
admin.site.register(Rating)
admin.site.register(User)
# Register your models here.
