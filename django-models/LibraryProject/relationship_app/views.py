from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library

def list_books(request):
    books = Book.objects.all()  # ✅ This line must match exactly
    return render(request, 'list_books.html', {'books': books})  # ✅ Exact template name

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
