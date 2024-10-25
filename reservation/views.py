from django.db import connection
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def get(self, request):
    username = request.COOKIES.get('username')
    daftar_reservasi = []

    with connection.cursor() as cursor:
        cursor.execute(
            f'SELECT * FROM reservasi WHERE pemesan = %s', [username])
        daftar_reservasi = cursor.fetchall()
    
    context = {
        'status': 'success',
        'daftar_reservasi': daftar_reservasi,
    }
    response = render(request, 'profile', context)
    return response

def post(self, request):
    username = request.COOKIES.get('username')
    wisata = request.GET.get('id_wisata')
    created_at = request.GET.get('timestamp')
    qty=1

    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT qty FROM reservasi WHERE username = %s AND wisata_id = %s',
            [username, wisata]
        )
        existing_reservasi = cursor.fetchone()

    if existing_reservasi:
        qty = existing_reservasi[0] + 1
        with connection.cursor() as cursor:
            cursor.execute(
                'UPDATE reservasi SET qty = %s WHERE username = %s AND wisata_id = %s',
                [qty, username, wisata]
            )

    else:
        qty = 1
        with connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO reservasi (wisata_id, created_at, username, qty) VALUES (%s, %s, %s, %s)',
                [wisata, created_at, username, qty]
            )
        
    connection.commit()
    return redirect('halaman wisata')