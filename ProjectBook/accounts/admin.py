from django.contrib import admin

# Register your models here.

# Register customer
from .models import Book, Staff, Supplier, Customer

admin.site.register(Book)
admin.site.register(Staff)
admin.site.register(Supplier)
admin.site.register(Customer)