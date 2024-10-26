from django.urls import path
from main.views import *
from . import views

app_name = 'main'

urlpatterns = [
    path('', show_landing, name='show_landing'),
    path('customer-reviews/', views.customer_reviews, name='customer_reviews'),
    path('login/', show_login, name='login'),  # Halaman login
    path('signup/', show_signup, name='signup'),  # Halaman signup
]