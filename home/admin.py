from django.contrib import admin
from .models import News, CommentsPostsModel, Category, Favorites

admin.site.register(News)
admin.site.register(Category)
admin.site.register(CommentsPostsModel)
admin.site.register(Favorites)
