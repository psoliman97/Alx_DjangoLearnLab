from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self) :
        return self.name
    
class Book(models.Model):
    name = models.CharField(max_length = 200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) :
        return self.title
    
class Liberary(models.Model):
    name = models.CharField(max_length = 100)
    books = models.ManyToManyField (Book)

    def __str__(self):
        return self.name
    
class Librarian(models.Model):
    name = models.CharField(max_length = 100)
    liberary = models.OneToOneField(Liberary, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
