from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,View
from .models import Book,BookCategory

# Create your views here.


def Books(request):
    all_books= Book.objects.all()
    return render(request, "books/all_books.html",{
            "books":all_books
        })

def books_category(resquest):
    return HttpResponse("hi from books category")

def bookDetailsView(resquest,slug):
    return HttpResponse("hi from books category")



# def starting_page(request):
#     all_books = Book.objects.all()
#     last_three_books= all_books.reverse()[:3]
#     return render(request,"books/index.html",{
#         "books":last_three_books
#     })


class StartingPageView(ListView):
    template_name = "books/index.html"
    model = Book
    ordering = ["-added_date"]
    context_object_name = "books"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


