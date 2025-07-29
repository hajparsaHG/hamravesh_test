from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import RandomString
import string
import random

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def write_random_string(request):
    rand_text = generate_random_string()
    rs = RandomString.objects.create(text=rand_text)
    return JsonResponse({'message': 'Random string saved', 'string': rs.text})

def read_latest_string(request):
    latest = RandomString.objects.last()
    return JsonResponse({'latest_string': latest.text if latest else None})