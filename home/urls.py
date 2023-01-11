from django.urls import path
from . import views


urlpatterns = [
    path('', views.NewsListView.as_view(), name='home'),
    path('<str:category_name>/', views.NewsListView.as_view(), name='home'),

    path('user/<int:pk>/', views.NewsUserListView.as_view(), name='news-user'),
    path('user/<int:pk>/category/<str:category_name>/', views.NewsUserListView.as_view(), name='news-user-category'),


    path('user/<int:pk>/favorites/', views.favorites_list, name='favorites-list'),
    path('user/<int:pk>/favorites/<str:category_name>/', views.favorites_list, name='favorites-list-category'),

    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/favorites/add/<int:pk>/', views.favorites_add, name='favorites-add'),


    path('news/<int:pk>/update/', views.NewsUpdateView.as_view(), name='news-update'),
    path('news/<int:pk>/delete/', views.NewsDeleteView.as_view(), name='news-delete'),
    path('news/created/', views.NewsCreateView.as_view(), name='news-created'),
]
