from email.policy import default
from django.db import models
from PIL import Image
# Create your models here.

# The models for database
class Book(models.Model):
    title = models.CharField(max_length=200)

    GENRE_CHOICES = [
        ('Math', 'Math'),
        ('Physics', 'Physics'),
        ('Biology', 'Biology'),
        ('Economy', 'Economy'),
        ('Geography', 'Geography'),
    ]
    genre = models.CharField(max_length=200, choices=GENRE_CHOICES, default='Math')

    quantity = models.PositiveIntegerField()
    description = models.CharField(max_length=200)

    thumbnail = models.ImageField(null=True)
    pdf = models.FileField(null=True)

    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Customer(models.Model):
    username = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    
    favorite_genre = models.CharField(max_length=200, choices=Book.GENRE_CHOICES, default='Math')
    balance = models.PositiveIntegerField(default=0)
    
    # genre_click_count = models.IntegerField(choices=Genre.choices)
    # owned_book = models.field

    def __str__(self):
        return self.username

class Supplier(models.Model):
    username = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    
    balance = models.PositiveIntegerField(default=0)
    
    # suplied_book = 

    def __str__(self):
        return self.username

class Staff(models.Model):
    username = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


# id
# username
# gmail
# favorite_genre
# genre_click_count: {
#     'Math': 4,
#     'physics': 2,
#     'biology': 1,
#     'economy': 2,

#     'total_click': 9
# }
# owned_book: [
#     'Purcel',
#     'Halliday'
# ]
# suplied_book: {
#     'Purcel': 20,
#     'Halliday: 30'
#     'total_supplied': 50
# }