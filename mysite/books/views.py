from django.shortcuts import render, redirect
from django.urls import reverse
from books.models import Book
from books.forms import BookForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
import datetime


@login_required
def all_books(request):
    books = Book.objects.all()
    return render(request, "books/index.html", context={"books": books})


@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    url = reverse("book.all")
    return redirect(url)


@login_required
def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(book.all_url)
    else:
        form = BookForm(instance=book)

    return render(request, "books/edit.html", {"form": form})


@login_required
def borrow_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.borrower = request.user
    book.return_date = datetime.date.today() + datetime.timedelta(days=7)
    book.save()
    url = reverse("book.all")
    return redirect(url)


@login_required()
def add(request):
    form = BookForm()

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            return redirect(book.all_url)

    return render(request, "books/add.html", {"form": form})


@login_required()
def borrowed_books(request):
    if request.user.username == "admin":
        books = Book.objects.filter(borrower__isnull=False)
    else:
        books = Book.objects.filter(borrower=request.user)
    return render(request, "books/borrowed.html", context={"books": books})


@login_required()
def return_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.return_date = None
    book.borrower = None
    book.save()
    url = reverse("book.borrowed")
    return redirect(url)
