from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Student

@login_required
def admin_dashboard(request):
    borrowed_books = Book.objects.filter(available_copies=0)
    all_books = Book.objects.all()
    all_users = Student.objects.all()
    return render(request, 'admin_module/dashboard.html', {
        'borrowed_books': borrowed_books,
        'all_books': all_books,
        'all_users': all_users,
    })

@login_required
def add_book(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            isbn=request.POST['isbn'],
            available_copies=request.POST['available_copies']
        )
        return redirect('admin_dashboard')
    return render(request, 'admin_module/add_book.html')

@login_required
def update_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.isbn = request.POST['isbn']
        book.available_copies = request.POST['available_copies']
        book.save()
        return redirect('admin_dashboard')
    return render(request, 'admin_module/update_book.html', {'book': book})

@login_required
def delete_book(request, book_id):
    Book.objects.get(id=book_id).delete()
    return redirect('admin_dashboard')
