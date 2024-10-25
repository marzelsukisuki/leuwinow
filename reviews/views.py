from django.shortcuts import render
from .models import CustomerReview

def customer_reviews(request):
    reviews = CustomerReview.objects.all()
    return render(request, 'reviews/customer_reviews.html', {'reviews': reviews})
