from django.shortcuts import render


def service_list(request):
    return render(request, "services/service_list.html")


def floor1(request):
    return render(request, "services/floor1.html")