from django.urls import path
from . import views

# for routing
urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('add/addbook/', views.addbook, name='addbook'),

    path('edit/<int:id>', views.edit, name='edit'),
    path('edit/editbook/<int:id>', views.editbook, name='editbook'),
    
    path('delete/<int:id>', views.delete, name='delete'),

    path('books/', views.books, name='books'),
    path('customers/', views.customers, name='customer'),

    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
