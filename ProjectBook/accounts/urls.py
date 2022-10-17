from django.urls import path
from . import views

# for routing
urlpatterns = [
    path('', views.home),
    path('add/', views.add),
    path('add/addbook/', views.addbook),

    path('edit/<int:id>', views.edit),
    path('edit/editbook/<int:id>', views.editbook),
    
    path('delete/<int:id>', views.delete),

    path('books/', views.books),
    path('customers/', views.customers),
]
