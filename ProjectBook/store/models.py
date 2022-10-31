from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    product_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=500, blank=True)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name



# Reccomendation
class AccountData(models.Model):
    username = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)


    GENRE_CHOICES = [
        ('Mathematics'      , 'Mathematics'     ),
        ('Physics'          , 'Physics'         ),
        ('Biology'          , 'Biology'         ),
        ('Economy'          , 'Economy'         ),
        ('Geography'        , 'Geography'       ),
        ('Chemistry'        , 'Chemistry'       ),
        ('English'          , 'English'         ),
        ('Computer-science' , 'Computer-science'),
        ('Other'            , 'Other'           ),
    ]
    
    favorite_category = models.CharField(max_length=200, choices=GENRE_CHOICES, default='Mathematics')
    # balance = models.PositiveIntegerField(default=0)

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
    

    def __str__(self):
        return self.username
