from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'superanota/home.html')