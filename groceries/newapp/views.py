from django.shortcuts import render
from .models import Item

# Create your views here.
def newapp(request):
    return render(request,
                  "newapp/newapp.html",
                  {'items': Item.objects.all()})