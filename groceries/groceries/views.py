from django.shortcuts import render

def homepage(request):
    return render(request, "home.html")

def inventory(request):
    return render(request, "inventory.html")