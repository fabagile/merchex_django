from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Listing


def listings(request):
    titles = Listing.objects.all()
    return HttpResponse(f""" 
     <h1 style="font-family: Arial">Mes stars préférées</h1>
     <h2>Dernières nouvelles</h2>
     <div>

        <div>{titles[0].title}</div>
        <div>{titles[1].title}</div>

        </div>
       """)


def hello(request):
    band = Band.objects.all()

    # band[2].name = "Alan Parsons Project"
    # band.save()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <ul>

        <li>{band[0].name}</li>
        <li>{band[1].name}</li>
        <li>{band[2].name}</li>
        </ul>

    """)


def about(request):
    return HttpResponse(
        '<h1>À propos de <em>nous</em></h1><p>on adoOore ce site !</p>')
