from django.shortcuts import render

def home(request):
    # Your view logic here
    return render(request, "index.html")

def dashboard(request):
    return render(request, "dashboard.html")
