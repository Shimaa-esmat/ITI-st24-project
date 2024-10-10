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
            return redirect('book_detail', book_id=book.id)
    else:
        form = BookForm(instance=book)

    return render(request, 'books/edit_book.html', {'form': form})
            
            
@login_required
def borrrow_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.borrwer = request.user
    
    
@login_required()
def add(request):
    form = BookForm() 

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES) 
        if form.is_valid():
            book = form.save()
            return redirect(book.all_url)

    return render(request, 'books/add.html', {'form': form})