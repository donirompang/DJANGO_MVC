from django.shortcuts import render
from .models import Mentee

def mentee(request):
    mentee = Mentee.objects.all()
    return render(request, 'mentee/mentee.html',{'mentee':mentee})
