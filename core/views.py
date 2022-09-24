from django.shortcuts import render
from core.models import Listing

# Create your views here.

def homepage(request,):
    listings = Listing.objects.all()
    context = {"data":listings}
    return render(request,template_name='core/base.html',context=context)
