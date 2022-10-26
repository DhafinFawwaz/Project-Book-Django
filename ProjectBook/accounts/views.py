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
            form = CreateUserForm(data=request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)


                username        = user
                # phone           = request.POST['phone']
                email           = form.cleaned_data.get('email')
                # date_created    = request.POST['date_created']
                favorite_genre  = request.POST.get('favorite_genre')
                # balance         = request.POST['balance']

                phone           = ''
                # email           = ''
                # date_created    = ''
                # favorite_genre  = ''
                balance         = 0

                customer = Customer(username = username, phone=phone, email=email, 
                                    favorite_genre=favorite_genre, balance=balance)
                customer.save()


                return redirect('login')
            else:
                messages.info(request, list(form.errors.values())[0])

        context = {'form': form, 'genres': Book.GENRE_CHOICES}
        return render(request, 'register.html', context)

def login_page(request):
    if request.user.is_authenticated: # if user is still logged in (already logged in after closing), redirect immediately
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
        return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    
    return redirect('login')


#endregion Login/Register

#region home
@login_required(login_url='login') # @ makes it so whenever home(request) get called, login_required is called first then home(request) get called. This makes only logged in user can view this
def home(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books.html', context)
#endregion home

#region book
@login_required(login_url='login') # @ makes it so whenever home(request) get called, login_required is called first then home(request) get called. This makes only logged in user can view this
def books(request):
    return render(request, 'books.html')

@login_required(login_url='login') # @ makes it so whenever home(request) get called, login_required is called first then home(request) get called. This makes only logged in user can view this
def add(request):
    choices = Book.GENRE_CHOICES
    context = {'choices': choices}


    # [Delete] for dummy data
    # for i in range(len(Book.GENRE_CHOICES)):
    #     for j in range(12):
    #         title = Book.GENRE_CHOICES[i][0]+" dummy "+str(j+1)
    #         genre = Book.GENRE_CHOICES[i][0]
    #         quantity = 1
    #         description = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    #         Maecenas aliquet odio commodo, pellentesque nunc id, gravida nunc. Nullam 
    #         in pretium urna, sed vestibulum nunc. Aliquam erat volutpat. Phasellus non 
    #         sapien quis velit pretium aliquam aliquet rutrum massa. Mauris scelerisque 
    #         tincidunt ante, quis commodo ipsum elementum sed. Nunc egestas leo ut velit 
    #         ultrices mattis. Mauris interdum consectetur velit, quis ultricies lorem 
    #         pellentesque ut. Donec nec convallis massa. Duis semper pretium consectetur. 
    #         In hac habitasse platea dictumst."""
    #         thumbnail = "./static/images/mountainchicken.jpg"
    #         pdf = "./static/pdf/PDFdummy.pdf"
    #         price = 50000

    #         book = Book(title=title, genre=genre, quantity=quantity, description=description, thumbnail=thumbnail, pdf=pdf, price=price)
    #         book.save()

    # [Delete]


    return render(request, 'add.html', context)
@login_required(login_url='login') # @ makes it so whenever home(request) get called, login_required is called first then home(request) get called. This makes only logged in user can view this
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

@login_required(login_url='login') # @ makes it so whenever home(request) get called, login_required is called first then home(request) get called. This makes only logged in user can view this
def edit(request, id):
    book = Book.objects.get(id=id)
    choices = Book.GENRE_CHOICES
    context = {'book': book, 'choices': choices}
    return render(request, 'edit.html', context)
@login_required(login_url='login') # @ makes it so whenever home(request) get called, login_required is called first then home(request) get called. This makes only logged in user can view this
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

@login_required(login_url='login') # @ makes it so whenever home(request) get called, login_required is called first then home(request) get called. This makes only logged in user can view this
def delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/') # Go back home

#endregion book

#region others
def supliers(request):
    return render(request, 'supliers.html')

@login_required(login_url='login') # @ makes it so whenever home(request) get called, login_required is called first then home(request) get called. This makes only logged in user can view this
def customers(request):
    total_show_amount = 12 #
    reccomendation_show_amount = 9 #
    # favorite_show_amount will be the rest. There may be a case where favorite_show_amount is 1 higher/lower than expected because of rounding value
    
    customer = Customer.objects.get(username=request.user)
    books = Book.objects.order_by('?').values_list('id', 'genre') # return tuples because more than 1 parameters. order_by('?) makes it random
    GENRE_CLICK_COUNT = (
        ('Math'             , customer.Math_click_count),
        ('Physics'          , customer.Physics_click_count),
        ('Biology'          , customer.Biology_click_count),
        ('Economy'          , customer.Economy_click_count),
        ('Geography'        , customer.Geography_click_count),
        ('Chemistry'        , customer.Chemistry_click_count),
        ('English'          , customer.English_click_count),
        ('Computer Science' , customer.ComputerScience_click_count),
        ('Other'            , customer.Other_click_count),
        ('Total'            , customer.Total_click_count),
    )
    books_genres = []
    for book in books:
        books_genres.append(book[1])
    
    books_genres_debug = {i:books_genres.count(i) for i in books_genres}
    
    
    books_reccomended_ids = []
    shown = 0

    # Reccomendation by click
    for i in range(len(GENRE_CLICK_COUNT) - 1): # Exclude 'Total'
        genre_books = tuple(
            filter(lambda item: item[1] == GENRE_CLICK_COUNT[i][0], books) # item[1] is books genre. GENRE_CLICK_COUNT[i][0] is the current genre to check
        )
        amount = round(GENRE_CLICK_COUNT[i][1]/customer.Total_click_count * reccomendation_show_amount)
        for i in range(amount):
            if i > len(genre_books)-1:
                break
            books_reccomended_ids.append(genre_books[i][0]) # Append only the title
            shown += 1

    # shuffle
    from random import shuffle
    shuffle(books_reccomended_ids)
    
    # Reccomendation by favorite genre (the rest)
    genre_books = tuple(
        filter(lambda item: item[1] == customer.favorite_genre, books)
    )
    i = 0
    while shown <= total_show_amount:
        books_reccomended_ids.insert(0, genre_books[i][0]) # Show reccomendation by favorite first. Append only the title.
        shown += 1
        i += 1

    # Query by list
    books_reccomended_unordered = Book.objects.filter(pk__in=books_reccomended_ids).order_by('?')
    
    # reorder
    books_reccomended = []
    for book in books_reccomended_unordered:
        if book.genre == customer.favorite_genre:
            books_reccomended.insert(0, book)
        else:
            books_reccomended.append(book)

    
    favorite_genre = customer.favorite_genre
    
    context = {'books_genres_debug': books_genres_debug, 'books_reccomended': books_reccomended, 'GENRE_CLICK_COUNT': GENRE_CLICK_COUNT, 'favorite_genre':favorite_genre}
    return render(request, 'customers.html', context)

@login_required(login_url='login') # @ makes it so whenever home(request) get called, login_required is called first then home(request) get called. This makes only logged in user can view this
def product_detail(request, id):
    book = Book.objects.get(id=id)
    customer = Customer.objects.get(username=request.user)
    
    if book.genre == 'Math': customer.Math_click_count += 1
    elif book.genre == 'Physics': customer.Physics_click_count += 1
    elif book.genre == 'Biology': customer.Biology_click_count += 1
    elif book.genre == 'Economy': customer.Economy_click_count += 1
    elif book.genre == 'Geography': customer.Geography_click_count += 1
    elif book.genre == 'Chemistry': customer.Chemistry_click_count += 1
    elif book.genre == 'English': customer.English_click_count += 1
    elif book.genre == 'Computer Science': customer.ComputerScience_click_count += 1
    elif book.genre == 'Other': customer.Other_click_count += 1

    customer.Total_click_count += 1
    customer.save()

    return redirect('/customers') 
#endregion others
