from django.shortcuts import render


# Create your views here.
from django.shortcuts import render


def haircare(request):
    return render(request, "category/haircare.html")


def makeup(request):
    return render(request, "category/makeup.html")


def medication(request):
    return render(request, "category/medication.html")


def babymom(request):
    return render(request, "category/Baby&Mom.html")


def skincare(request):
    return render(request, "category/skincare.html")
