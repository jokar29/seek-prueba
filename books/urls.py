from django.urls import path
from .views import BookList
from django.urls import path
from .views import BookList, BookDetail, AveragePriceByYear

urlpatterns = [
    path('api/books/', BookList.as_view(), name='book-list'),
    path('api/books/<str:book_id>/', BookDetail.as_view(), name='book-detail'),
    path("books/average-price/<int:year>/", AveragePriceByYear.as_view(), name="average-price-by-year"),
]