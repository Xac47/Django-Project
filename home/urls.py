from django.urls import path
from . import views


urlpatterns = [
    path('', views.NewsListView.as_view(), name='home'),
    path('user/<int:id>/', views.NewsUserListView.as_view(), name='news-user'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/<int:pk>/update/', views.NewsUpdateView.as_view(), name='news-update'),
    path('news/<int:pk>/delete/', views.NewsDeleteView.as_view(), name='news-delete'),
    path('news/<int:pk>/comments/', views.CommentNewsCreateView.as_view(), name='news-comments'),
    path('news/created/', views.NewsCreateView.as_view(), name='news-created'),
]
