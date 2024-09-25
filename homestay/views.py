from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def repair(request):
    return render(request, "repair.html")

def replace(request):
    return render(request, "replace.html")

def complain(request):
    return render(request, "complain.html")

def aircond_log(request):
    return render(request, "aircond_log.html")

def refill_log(request):
    return render(request, "refill_log.html")