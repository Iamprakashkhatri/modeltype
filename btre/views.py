from django.shortcuts import render
from .models import Listing,Realtor

def listing_select_related(request):
    #it access all the data
    # listing = Listing.objects.all()
    #to access data from manyside of relation,it is for one to one and one to many,it access only the relavent data
    # using inner join.
    listing = Listing.objects.select_related('realtor').all()
    #to access data from one side of relation, it is for many to many
    # listing = Realtor.objects.prefetch_related('listings')
    print(listing)
    return render (request,'btre/home.html',{'listing':listing})
def ormquery(request):
    queryset = Realtor.objects.filter(name__startswith='R')
    print(queryset)
    return render(request, 'btre/home.html', {})
