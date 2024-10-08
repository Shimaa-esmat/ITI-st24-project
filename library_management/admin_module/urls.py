from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add_book/', views.add_book, name='add_book'),
    path('update_book/<int:book_id>/', views.update_book, name='update_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]
