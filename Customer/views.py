from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse


def register(request):
    return render(request, 'Registration.html')
    return HttpResponse()

# Create your views here.
