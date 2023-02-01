from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band


def hello(request):
    band = Band.objects.all()
    # band[2].name = "Alan Parsons Project"
    # band.save()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <div>
        <div>{band[0].name}</div>
        <div>{band[1].name}</div>
        <div>{band[2].name}</div>
        </div>

    """)


def about(request):
    return HttpResponse(
        '<h1>À propos de <em>nous</em></h1><p>on adoOore ce site !</p>')
