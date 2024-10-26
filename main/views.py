from django.shortcuts import render
from .models import CustomerReview
# Create your views here.
def show_landing(request):
    return render(request, 'index.html')

# def customer_reviews(request):
#     reviews = CustomerReview.objects.all()
#     return render(request, 'customer_reviews.html', {'reviews': reviews})


def customer_reviews(request):
    reviews = CustomerReview.objects.all()
    
    # Menyiapkan bintang sebagai atribut tambahan
    for review in reviews:
        review.stars = '★' * review.rating + '☆' * (5 - review.rating)

    return render(request, 'reviews/customer_reviews.html', {'reviews': reviews})

def show_login(request):
    return render(request, 'login.html')

def show_signup(request):
    return render(request, 'signup.html')