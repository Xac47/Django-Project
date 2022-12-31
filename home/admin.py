from django.contrib import admin
from .models import News, CommentsPostsModel, Category

admin.site.register(News)
admin.site.register(Category)
admin.site.register(CommentsPostsModel)
