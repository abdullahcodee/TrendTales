from django.urls import path
from .import views

urlpatterns = [
    path("",views.StartingPageView.as_view(), name="starting_page" ),
    path("books",views.Books, name="books" ),
    path("books/<slug:slug>/", views.bookDetailsView,name="book-details"),
    path("books/category/", views.books_category,name="books-category"),
]