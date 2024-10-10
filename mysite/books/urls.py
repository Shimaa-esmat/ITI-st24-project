from django.urls import path
from books.views import add ,delete_book , update_book, borrrow_book, all_books

urlpatterns = [
    path('',all_books, name='book.all'),
    path('add',add, name='book.add'),
    path('delete/<int:book_id>',delete_book, name='book.delete'),
    path('update/<int:book_id>',update_book, name='book.update'),
    path('borrrow/<int:book_id>',borrrow_book, name='book.borrrow'),
]
