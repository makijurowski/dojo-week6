# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse, get_object_or_404, redirect, render
from django_tables2 import RequestConfig
from .models import *
from .tables import *


def index(request):
    """
    User dashboard page that shows latest reviews and list of all reviews
    @ /reviews/books/index
    """
    response = "Placeholder to verify reviews app creation."
    return HttpResponse(response)

def review_list(request):
    all_reviews_list = Review.objects.all()
    latest_reviews_list = Review.objects.order_by('-created_at')[:3]
    return render(request, 'reviews/review_list.html', {'all_reviews': all_reviews_list, 'latest_reviews': latest_reviews_list})

def book_list(request):
    table = BooksTable(Book.objects.all())
    context = {
        'table': table,
    }
    RequestConfig(request).configure(table)
    return render(request, 'reviews/book_list.html', context)

def new_review(request):
    """
    Shows form to add a new book and/or new book review @ reviews/books/new/
    Includes: book title, author (choose from list AND add new), review description, star rating
    """
    pass

def view_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'review_detail.html', {'review': review})


def view_book(request):
    """
    Displays individual book details at reviews/books/<id> & allows user to add/delete a review for the given book
    Includes: title, author, reviews
    """
    review = get_object_or_404(Book, pk=book_id)
    return render(request, 'review_detail.html', {'book': book})


def delete_review(request):
    """
    Processes logged in user deleting their own review @ reviews/books/delete
    """
    pass


def post_review(request):
    """
    Processes post data for a new review @ reviews/books/post
    """
    pass
