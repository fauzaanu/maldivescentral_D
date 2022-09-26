from django.shortcuts import render, redirect
from core.models import Listing, Cat

# Create your views here.

def homepage(request,):
    listings = Listing.objects.all()
    cats = Cat.objects.all()
    context = {"data":listings, 'cats':cats}
    return render(request,template_name='core/home.html',context=context)

def homepage_filtered(request,catname):
    listings = Listing.objects.filter(listing_category__category_slug=catname)
    cats = Cat.objects.all()
    context = {"data":listings, 'cats':cats}
    return render(request,template_name='core/base.html',context=context)


def add_view(request):
    return render(request, template_name='core/add.html',)


def adder_view(request):
    name = "a"
    link = "a"
    if request.POST:
        name = request.POST['name']
        link = request.POST['link']

    print(name,link)

    import requests
    def warningsystem(msg):
        # print("warning system") # FOR DEBUG
        tg_chat_id = '996280547'  # TELEGRAM CHAT ID : USE https://t.me/MyChatInfoBot or manually call /getupdates
        tapi_key = "5733560694:AAHfrYrTAlsh-El8bZBX-slSRlosq2Yz4oE"  # API KEY THAT BOT FATHER GIVES..
        x = requests.get(f"https://api.telegram.org/bot{tapi_key}/sendMessage?chat_id={tg_chat_id}&text={msg}")
        # return x # FOR DEBUG

    warningsystem(f"New listing Name={name}, Link={link}")

    return redirect('home')

def searchview(request):
    search_query = ''
    if request.GET.get('query'):
        search_query = request.GET['query']

    #print('SEARCH',search_query)

    listings = Listing.objects.filter(listing_description__icontains=search_query)
    context = {"data": listings}
    return render(request,template_name='core/base.html',context=context)
