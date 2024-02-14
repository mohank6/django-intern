from django.shortcuts import render
from django.http import HttpResponse

# from .. import fake_data


def home(request):
    # fake_data.generate_fake_data()
    return HttpResponse("Home")
