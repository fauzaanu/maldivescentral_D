from django.shortcuts import render
from core.models import Listing

# Create your views here.

def homepage(request,):
    listings = Listing.objects.all()
    context = {"data":listings}
    return render(request,template_name='core/base.html',context=context)

def searchview(request):
    search_query = ''
    if request.GET.get('query'):
        search_query = request.GET['query']

    #print('SEARCH',search_query)

    listings = Listing.objects.filter(listing_description__icontains=search_query)
    context = {"data": listings}
    return render(request,template_name='core/base.html',context=context)
