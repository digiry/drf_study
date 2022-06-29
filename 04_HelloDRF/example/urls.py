from django.urls import path
from example.views import (
    helloAPI,
    booksAPI,
    bookAPI,
    BookAPI,
    BooksAPI,
    BooksAPIMixins,
    BookAPIMixins,
)

urlpatterns = [
    path("hello/", helloAPI),
    path("fbv/books/", booksAPI),
    path("fbv/book/<int:bid>/", bookAPI),
    path("cbv/books/", BooksAPI.as_view()),
    path("cbv/book/<int:bid>/", BookAPI.as_view()),
    path("mixin/books/", BooksAPIMixins.as_view()),
    path("mixin/book/<int:bid>/", BookAPIMixins.as_view()),
]
