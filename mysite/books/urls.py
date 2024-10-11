from django.urls import path
from books.views import (
    add,
    delete_book,
    update_book,
    borrow_book,
    all_books,
    return_book,
    borrowed_books,
)

urlpatterns = [
    path("", all_books, name="book.all"),
    path("add", add, name="book.add"),
    path("delete/<int:book_id>", delete_book, name="book.delete"),
    path("update/<int:book_id>", update_book, name="book.update"),
    path("borrow/<int:book_id>", borrow_book, name="book.borrow"),
    path("borrowed/", borrowed_books, name="book.borrowed"),
    path("return/<int:book_id>", return_book, name="book.return"),
]
