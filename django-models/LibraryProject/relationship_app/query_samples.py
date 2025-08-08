import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')  # Adjust if your project name is different
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Optional: create sample data
def create_sample_data():
    author = Author.objects.create(name="George Orwell")
    book1 = Book.objects.create(title="1984", author=author)
    book2 = Book.objects.create(title="Animal Farm", author=author)

    library = Library.objects.create(name="Central Library")
    library.books.set([book1, book2])

    Librarian.objects.create(name="Alice", library=library)

# Required Queries
def queries():
    # 1. Query all books by a specific author
    author_name = "George Orwell"
    author = Author.objects.get(name=author_name)  # << this line uses .get()
    books_by_author = Book.objects.filter(author=author)  # << this line uses .filter()
    print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

    # 2. List all books in a library
    library_name = "Central Library"
    library = Library.objects.get(name=library_name)
    print(f"Books in {library_name}: {[book.title for book in library.books.all()]}")

    # 3. Retrieve the librarian for a library
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian at {library_name}: {librarian.name}")

if __name__ == "__main__":
    create_sample_data()  # Comment this line if sample data already exists
    queries()
