from bookshelf.models import Book

updated_book.delete()
print(Book.objects.all())
# Output: <QuerySet []>
