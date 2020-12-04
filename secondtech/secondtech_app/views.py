from django.shortcuts import render


# Create your views here.
from secondtech_app.models import Device


def homepage(request):
    return render(request, 'landing_page.html')


def about_page(request):
    return render(request, 'about_us.html')


def view_devices(request):
    context = {
        'devices': Device.objects.all()
    }

    return render(request, 'all_devices.html', context)