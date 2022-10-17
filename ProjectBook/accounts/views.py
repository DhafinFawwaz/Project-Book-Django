from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout # as the name says
from django.contrib import messages # valid/invalid user message when registering/login
from django.contrib.auth.decorators import login_required # redirect to login_page if not logged in
# Create your views here.
from .models import *
from .forms import OrderForm, CreateUserForm

#region Login/Register
def register_page(request):
    if request.user.is_authenticated: # if still user is still logged in (already logged in after closing), redirect immediately
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)

def login_page(request):
    if request.user.is_authenticated: # if still user is still logged in (already logged in after closing), redirect immediately
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username Or password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)

def logout_user(request):
    logout(request)
    
    return redirect('login')


#endregion Login/Register

#region home
# @login_required(login_url='login') # @ makes it so whenever home(request) get called, login_required is called first then home(request) get called. This makes only logged in user can view this
def home(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'accounts/books.html', context)
#endregion home

#region book
# @login_required(login_url='login') # @ makes it so whenever home(request) get called, login_required is called first then home(request) get called. This makes only logged in user can view this
def books(request):
    return render(request, 'accounts/books.html')

# @login_required(login_url='login') # @ makes it so whenever home(request) get called, login_required is called first then home(request) get called. This makes only logged in user can view this
def add(request):
    choices = Book.GENRE_CHOICES
    context = {'choices': choices}
    return render(request, 'accounts/add.html', context)
# @login_required(login_url='login') # @ makes it so whenever home(request) get called, login_required is called first then home(request) get called. This makes only logged in user can view this
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
    return redirect('home') # Go back home

# @login_required(login_url='login') # @ makes it so whenever home(request) get called, login_required is called first then home(request) get called. This makes only logged in user can view this
def edit(request, id):
    book = Book.objects.get(id=id)
    choices = Book.GENRE_CHOICES
    context = {'book': book, 'choices': choices}
    return render(request, 'accounts/edit.html', context)
# @login_required(login_url='login') # @ makes it so whenever home(request) get called, login_required is called first then home(request) get called. This makes only logged in user can view this
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
    return redirect('/') # Go back home

# @login_required(login_url='login') # @ makes it so whenever home(request) get called, login_required is called first then home(request) get called. This makes only logged in user can view this
def delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/') # Go back home

#endregion book

#region others
def supliers(request):
    return render(request, 'accounts/supliers.html')

def customers(request):
    return render(request, 'accounts/customers.html')
#endregion others

