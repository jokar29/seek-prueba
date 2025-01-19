from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList

from django.urls import path
from .views import BookList
from .views import BookDetail

urlpatterns = [
    path('api/books/', BookList.as_view(), name='book-list'),
    path('api/books/<str:book_id>/', BookDetail.as_view(), name='book-detail'),
]