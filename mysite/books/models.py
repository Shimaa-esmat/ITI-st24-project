from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to="books/images", null=True)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    return_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.title}"

    @property
    def image_url(self):
        return f"/media/{self.image}"

    @property
    def all_url(self):
        url = reverse("book.all")
        return url

    @property
    def edit_url(self):
        url = reverse("book.update", args=[self.id])
        return url

    @property
    def delete_url(self):
        url = reverse("book.delete", args=[self.id])
        return url

    @property
    def borrow_url(self):
        url = reverse("book.borrow", args=[self.id])
        return url
