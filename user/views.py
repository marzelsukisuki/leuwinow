from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.db import DatabaseError, connection
import datetime
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM user u WHERE u.username = %s AND u.password = %s", [username, password])
            user = cursor.fetchone()

        if user:
            request.session['username'] = user[0]
            response = redirect(reverse('main:show_landing'))

            response.set_cookie('username', user[0])
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, 'Username atau Password salah. Silahkan coba lagi')

    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        nama_lengkap = request.POST.get('nama_lengkap')
        email = request.POST.get('email')
        password = request.POST.get('password')

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM user WHERE email = %s", [email])
            emails = cursor.fetchall()
        if emails:
            context = {
                'form': request.POST,
                'error': "Username sudah terdaftar di sistem."
            }
            return render(request, 'register.html', context)

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO pengguna (username, nama_lengkap, email, password) VALUES (%s, %s, %s, %s)", [username, nama_lengkap, email, password])

        return redirect('user:login')

    return render(request, 'register.html')