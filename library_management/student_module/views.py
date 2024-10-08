from django.shortcuts import render, redirect
from .models import BorrowedBook
from admin_module.models import Book, Student

def register(request):
    if request.method == 'POST':
        # Implement student registration
        return redirect('student_dashboard')
    return render(request, 'student_module/register.html')

@login_required
def student_dashboard(request):
    borrowed_books = BorrowedBook.objects.filter(student=request.user.student)
    return render(request, 'student_module/dashboard.html', {'borrowed_books': borrowed_books})

@login_required
def borrow_book(request, book_id):
    book = Book.objects.get(id=book_id)
    BorrowedBook.objects.create(book=book, student=request.user.student)
    return redirect('student_dashboard')

@login_required
def return_book(request, borrowed_book_id):
    borrowed_book = BorrowedBook.objects.get(id=borrowed_book_id)
    borrowed_book.return_date = timezone.now()
    borrowed_book.save()
    return redirect('student_dashboard')
