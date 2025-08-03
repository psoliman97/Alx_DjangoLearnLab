from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book

from django.contrib.auth import login

from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

from django.contrib.auth.decorators import permission_required

relationship_app.can_add_book
relationship_app.can_change_book
relationship_app.can_delete_book

## I don't know what is this?
UserCreationForm()


##
def is_Admin(user):
    return user.is_authenticated and user.role == 'Admin'

@login_required
@user_passes_test(is_Admin)
def Admin_only_view(request):
    return render(request, 'admin_view.html')
##


# relationship_app/views.py
# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'books_list': books}
    return render(request, "relationship_app/list_books.html", context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = 'library' 

 
def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['books'] = self.object.books.all()
    return context


def register (createview):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'



def is_admin(user):
    return user.userprofile.role == 'Admin'


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

def is_librarian(user):
    return user.userprofile.role == 'Librarian'


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


