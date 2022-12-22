from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from.models import Member
# Create your views here.

def demo(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'result':obj})
def demo(request):
    obj1=Member.objects.all()
    return render(request,"index.html",{'result1':obj1})


