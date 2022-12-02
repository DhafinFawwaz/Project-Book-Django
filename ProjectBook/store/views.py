from django.shortcuts import render, get_object_or_404
from .models import Product, AccountData
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
# Create your views here.

def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
        
        
        # Reccomendation
        if request.user.is_authenticated == True:
            account_data = AccountData.objects.get(email=request.user)
            
            if   str(single_product.category) == 'Mathematics': account_data.Math_click_count += 1
            elif str(single_product.category) == 'Physics': account_data.Physics_click_count += 1
            elif str(single_product.category) == 'Biology': account_data.Biology_click_count += 1
            elif str(single_product.category) == 'Economy': account_data.Economy_click_count += 1
            elif str(single_product.category) == 'Geography': account_data.Geography_click_count += 1
            elif str(single_product.category) == 'Chemistry': account_data.Chemistry_click_count += 1
            elif str(single_product.category) == 'English': account_data.English_click_count += 1
            elif str(single_product.category) == 'Computer-science': account_data.ComputerScience_click_count += 1
            elif str(single_product.category) == 'Other': account_data.Other_click_count += 1

            account_data.Total_click_count += 1
            account_data.save()
    
    
    
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    return render(request, 'store/product_detail.html', context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)