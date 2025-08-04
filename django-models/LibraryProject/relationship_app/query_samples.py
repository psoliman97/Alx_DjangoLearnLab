import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Example setup (optional - create sample data)
def create_sample_data():
    author = Author.objects.create(name="George Orwell")
    book1 = Book.objects.create(title="1984", author=author)
    book2 = Book.objects.create(title="Animal Farm", author=author)

    library = Library.objects.create(name="Central Library")
    library.books.set([book1, book2])

    Librarian.objects.create(name="Alice", library=library)

# Queries

def queries():
    # Query all books by a specific author
    author_name = "George Orwell"
    books_by_author = Book.objects.filter(author__name=author_name)
    print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

    # List all books in a library
    library_name = "Central Library"
    library = Library.objects.get(name=library_name)
    print(f"Books in {library_name}: {[book.title for book in library.books.all()]}")

    # Retrieve the librarian for a library
    librarian = Librarian.objects.get(library__name=library_name)
    print(f"Librarian at {library_name}: {librarian.name}")

if __name__ == "__main__":
    create_sample_data()  # comment this line if you already have data
    queries()
