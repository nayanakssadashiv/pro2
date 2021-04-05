from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index2(request):
    return HttpResponse("<h1>index of app2</h1>")
def rend_app2(request):
    return render(request,"app2/sample2.html")
