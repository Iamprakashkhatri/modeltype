from django.shortcuts import render
from .models import Book
def book_list(request):
    queryset = Book.objects.all()

    books = []
    for book in queryset:
        books.append({'id': book.id, 'name': book.name, 'publisher': book.publisher.name})

    print (books)
    return render(request,"home.html",{})
