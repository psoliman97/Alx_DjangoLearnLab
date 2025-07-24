retrieved_book = Book.objects.get(id=book.id)
print(retrieved_book.title)
print(retrieved_book.author)
print(retrieved_book.publication_year)
# Output:
# 1984
# George Orwell
# 1949
