from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library

# ✅ Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # <- this line must exist
    return render(request, 'list_books.html', {'books': books})  # <- this template will be searched in your templates folder

# ✅ Class-based view to show library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
