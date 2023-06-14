from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    return render(request,"index.html")
#def about(request):
#    return render(request,"about.html")
#def value(request):
#    name="Addition"
#    return render(request,"home.html",{'obj':name})
#def addition(request):
#    x=int(request.GET["num1"])
#    y=int(request.GET["num2"])
#    res=x+y
#    return render(request,"result.html",{'result':res})
