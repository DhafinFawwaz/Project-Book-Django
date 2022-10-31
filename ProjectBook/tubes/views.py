from django.shortcuts import render
from store.models import Product, AccountData
from category.models import Category
from django.contrib.auth.decorators import login_required

@login_required(login_url = 'login')
def home(request):
    # ------------- Reccomendation -------------
# region reccomendation
    total_show_amount = 8 # 12
    reccomendation_show_amount = 8 # orignally 9, but favorite_genre hasn't been implemented yet
    # favorite_show_amount will be the rest. There may be a case where favorite_show_amount is 1 higher/lower than expected because of rounding value
    
    products_id_category = Product.objects.order_by('?').filter(is_available=True).values_list("id", "category") # return tuples because more than 1 parameters. order_by('?) makes it random
    # for some reason, values_list return a number and not a string
    
    account_data = AccountData.objects.get(email=request.user)
    # only query the id and category because querying images will take more time

    GENRE_CLICK_COUNT = list(Category.objects.all().values_list("category_name", "id"))

    for i in range(len(GENRE_CLICK_COUNT)):
        if   GENRE_CLICK_COUNT[i][0] == 'Mathematics':         GENRE_CLICK_COUNT[i] = (GENRE_CLICK_COUNT[i][0], GENRE_CLICK_COUNT[i][1], account_data.Math_click_count)
        elif GENRE_CLICK_COUNT[i][0] == 'Physics':             GENRE_CLICK_COUNT[i] = (GENRE_CLICK_COUNT[i][0], GENRE_CLICK_COUNT[i][1], account_data.Physics_click_count)
        elif GENRE_CLICK_COUNT[i][0] == 'Biology':             GENRE_CLICK_COUNT[i] = (GENRE_CLICK_COUNT[i][0], GENRE_CLICK_COUNT[i][1], account_data.Biology_click_count)
        elif GENRE_CLICK_COUNT[i][0] == 'Economy':             GENRE_CLICK_COUNT[i] = (GENRE_CLICK_COUNT[i][0], GENRE_CLICK_COUNT[i][1], account_data.Economy_click_count)
        elif GENRE_CLICK_COUNT[i][0] == 'Geography':           GENRE_CLICK_COUNT[i] = (GENRE_CLICK_COUNT[i][0], GENRE_CLICK_COUNT[i][1], account_data.Geography_click_count)
        elif GENRE_CLICK_COUNT[i][0] == 'Chemistry':           GENRE_CLICK_COUNT[i] = (GENRE_CLICK_COUNT[i][0], GENRE_CLICK_COUNT[i][1], account_data.Chemistry_click_count)
        elif GENRE_CLICK_COUNT[i][0] == 'English':             GENRE_CLICK_COUNT[i] = (GENRE_CLICK_COUNT[i][0], GENRE_CLICK_COUNT[i][1], account_data.English_click_count)
        elif GENRE_CLICK_COUNT[i][0] == 'Computer-science':    GENRE_CLICK_COUNT[i] = (GENRE_CLICK_COUNT[i][0], GENRE_CLICK_COUNT[i][1], account_data.ComputerScience_click_count)
        elif GENRE_CLICK_COUNT[i][0] == 'Other':               GENRE_CLICK_COUNT[i] = (GENRE_CLICK_COUNT[i][0], GENRE_CLICK_COUNT[i][1], account_data.Other_click_count)
    # GENRE_CLICK_COUNT: [(name, id, click_count)]

    
    products_category = [] # Fill this with only Product.category
    for product in products_id_category:
        products_category.append(product[1])
    
    
    products_reccomended_ids = []

    # Reccomendation by click
    for i in range(len(GENRE_CLICK_COUNT) - 1): # Exclude 'Total'
        products_with_category = tuple(
            filter(lambda item: item[1] == GENRE_CLICK_COUNT[i][1], products_id_category) # item[1] is products category. GENRE_CLICK_COUNT[i][0] is the current category to check
        )# item[1] somehow becomes the id of category (int), not the name (string)

        # genre_products will get filled with everybook that has a certain genre
        # for example genre_products = [(1342685, 'Mathematics'), (3244857, 'Mathematics'), (0795483, 'Mathematics'), (1260973, 'Mathematics')]
        amount = round(GENRE_CLICK_COUNT[i][2]/account_data.Total_click_count * reccomendation_show_amount)
        # the amount of product of the current category

        for i in range(amount):
            if i > len(products_with_category)-1:
                break
            products_reccomended_ids.append(products_with_category[i][0]) # Append only the title

    while len(products_reccomended_ids) > total_show_amount: # this can happen because of rounding
        products_reccomended_ids.pop(0)


    print("products_reccomended_ids")
    print(products_reccomended_ids)
    # shuffle
    from random import shuffle
    shuffle(products_reccomended_ids)

    
    
    # Reccomendation by favorite genre (the rest)
    def category_to_id(category_str): # input string
        category_id = 0
        for d in GENRE_CLICK_COUNT:
            if category_str == d[0]:
                category_id = d[1]
                break
        return category_id

    products_with_category = tuple(
        filter(lambda item: item[1] == category_to_id(account_data.favorite_category), products_id_category)
    )

    i = 0
    while len(products_reccomended_ids) < total_show_amount:
        if i > len(products_with_category)-1: # when there's not enough favorite product to show until it becomes total_show_amount
            break # this will happen with category that has so little book like geography
        products_reccomended_ids.insert(0, products_with_category[i][0]) # Show reccomendation by favorite first. Append only the title.
        i += 1
    

    # Query by list
    products_reccomended_unordered = Product.objects.filter(pk__in=products_reccomended_ids).order_by('?')
    
    #if still not enough
    from random import sample
    difference = total_show_amount - len(products_reccomended_unordered)
    while(difference > 0):
        id_only = [item[0] for item in list(products_id_category)]
        remainder = sample(list(id_only), difference) + list(products_reccomended_ids)

        products_reccomended_unordered = Product.objects.filter(pk__in=remainder).order_by('?')
        
        difference = total_show_amount - len(products_reccomended_unordered)
    

    

    # reorder
    products = [] # the main result that will go into context
    for product in products_reccomended_unordered:
        if str(product.category) == str(account_data.favorite_category): # somehow it needs to be converted to string
            products.insert(0, product)
        else:
            products.append(product)

    

    # Only 'products': products is usefull, the rest is for debugging    
    context = {'products': products}
    
    
    return render(request, 'home.html', context)
# endregion reccomendation
    # ------------- Reccomendation End -------------


    
