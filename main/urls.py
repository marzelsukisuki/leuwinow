from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_landing, name='show_landing'),
] 