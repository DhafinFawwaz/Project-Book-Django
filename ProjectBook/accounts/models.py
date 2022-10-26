from email.policy import default
from django.db import models
from PIL import Image
# Create your models here.

# The models for database
class Book(models.Model):
    title = models.CharField(max_length=200)

    GENRE_CHOICES = [
        ('Math'             , 'Math'            ),
        ('Physics'          , 'Physics'         ),
        ('Biology'          , 'Biology'         ),
        ('Economy'          , 'Economy'         ),
        ('Geography'        , 'Geography'       ),
        ('Chemistry'        , 'Chemistry'       ),
        ('English'          , 'English'         ),
        ('Computer Science' , 'Computer Science'),
        ('Other'            , 'Other'           ),
    ]
    genre = models.CharField(max_length=200, choices=GENRE_CHOICES, default='Math')

    quantity = models.PositiveIntegerField()
    description = models.CharField(max_length=1000)

    thumbnail = models.ImageField(null=True)
    pdf = models.FileField(null=True)

    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title + ' [' + self.genre +']'

class Customer(models.Model):
    username = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    
    favorite_genre = models.CharField(max_length=200, choices=Book.GENRE_CHOICES, default='Math')
    balance = models.PositiveIntegerField(default=0)

    Math_click_count            = models.PositiveIntegerField(default=1) # default to 1 to prevent division by 0
    Physics_click_count         = models.PositiveIntegerField(default=1)
    Biology_click_count         = models.PositiveIntegerField(default=1)
    Economy_click_count         = models.PositiveIntegerField(default=1)
    Geography_click_count       = models.PositiveIntegerField(default=1)
    Chemistry_click_count       = models.PositiveIntegerField(default=1)
    English_click_count         = models.PositiveIntegerField(default=1)
    ComputerScience_click_count = models.PositiveIntegerField(default=1)
    Other_click_count           = models.PositiveIntegerField(default=1)
    Total_click_count           = models.PositiveIntegerField(default=9)

    # GENRE_CLICK_COUNT = {
    #     'Math'            : Math_click_count,
    #     'Physics'         : Physics_click_count,
    #     'Biology'         : Biology_click_count,
    #     'Economy'         : Economy_click_count,
    #     'Geography'       : Geography_click_count,
    #     'Chemistry'       : Chemistry_click_count,
    #     'English'         : English_click_count,
    #     'ComputerScience' : ComputerScience_click_count,
    #     'Other'           : Other_click_count,
    # }


    
    # genre_click_count = models.IntegerField(choices=Genre.choices)
    # owned_book = models.field
    # def add_click_count(genre, amount):
    #     GENRE_CLICK_COUNT[genre]

    

    def __str__(self):
        return self.username

def add_click_count(genre, amount):
    if genre == 'Math':
        return Customer.Math_click_count
    elif genre == 'Physics':
        return Customer.Physics_click_count

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