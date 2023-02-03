from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Listing


def listings(request):
    titles = Listing.objects.all()
    return render(request, 'listings/listings.html', {
        "listings": titles
    })


def hello(request):
    bands = Band.objects.all()

    # band[2].name = "Alan Parsons Project"
    # band.save()
    return render(request, 'listings/hello.html', {
        'bands': bands
    })


def about(request):
    return render(request, 'listings/about.html')


def contact(request):
    return render(request, 'listings/contact.html')
