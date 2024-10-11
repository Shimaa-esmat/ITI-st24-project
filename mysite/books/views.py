from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from books.models import Book
from books.forms import BookForm
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import  login_required
import datetime
from django.contrib.auth.models import User


@login_required
def all_books(request):
    books =Book.objects.all()
    print("I got here")
    return  render(request, 'books/index.html',
                   context={"books": books})

@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    url  = reverse("book.all") # return with url ---> name --> students.index --> /students/
    return  redirect(url)

@login_required
def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(book.all_url)
    else:
        form = BookForm(instance=book)

    return render(request, 'books/add.html', {'form': form})
            
            
@login_required
def borrrow_book(request, book_id):
    book = Book.objects.get(id=book_id)
    borrower =  User.objects.get(id = request.user.id)
    book.borrwer = borrower
    print('----------------------------')
    print(borrower.username)
    print('----------------------------')

    book.return_date = datetime.date.today()+datetime.timedelta(days=7)
    book.save()
    url  = reverse("book.all") 
    return  redirect(url) 
    
    
@login_required()
def add(request):
    form = BookForm() 

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES) 
        if form.is_valid():
            book = form.save()
            return redirect(book.all_url)

    return render(request, 'books/add.html', {'form': form})

@login_required()
def borrowed_books(request):
    books = Book.objects.filter( borrower= request.user)
    
    return render(request, 'books/borrowed.html',context={"books": books})
    
    
def return_book(request,book_id):
    book = get_object_or_404(Book, id=book_id)
    book.return_date = None
    book.borrower = None
    book.save()
    url  = reverse("book.borrowed") # return with url ---> name --> students.index --> /students/
    return  redirect(url)