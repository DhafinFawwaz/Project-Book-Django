from turtle import pd
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
# Create your views here.

# views after routing
def home(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'accounts/books.html', context)

def books(request):
    return render(request, 'accounts/books.html')

def add(request):
    choices = Book.GENRE_CHOICES
    context = {'choices': choices}
    return render(request, 'accounts/add.html', context)
def addbook(request):
    title = request.POST['title']
    genre = request.POST['genre']
    quantity = request.POST['quantity']
    description = request.POST['description']
    thumbnail = request.POST['thumbnail']
    pdf = request.POST['pdf']
    price = request.POST['price']

    book = Book(title=title, genre=genre, quantity=quantity, description=description, thumbnail=thumbnail, pdf=pdf, price=price)
    book.save()

    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'accounts/books.html', context) # Go back home

def edit(request, id):
    book = Book.objects.get(id=id)
    choices = Book.GENRE_CHOICES
    context = {'book': book, 'choices': choices}
    return render(request, 'accounts/edit.html', context)
def editbook(request, id):
    title = request.POST['title']
    genre = request.POST['genre']
    quantity = request.POST['quantity']
    description = request.POST['description']
    thumbnail = request.POST['thumbnail']
    pdf = request.POST['pdf']
    price = request.POST['price']

    book = Book.objects.get(id=id)
    book.title = title
    book.genre = genre
    book.quantity = quantity
    book.description = description
    book.thumbnail = thumbnail
    book.pdf = pdf
    book.price = price
    
    book.save()

    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'accounts/books.html', context) # Go back home

def delete(request, id):
    return

def supliers(request):
    return render(request, 'accounts/supliers.html')


def customers(request):
    return render(request, 'accounts/customers.html')