from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from secondtech_app.models import Device


def view_admin_landing_page(request):
    if not request.user.is_superuser:
        return HttpResponse('<h1>You are not authorized!</h1>')
    return render(request, 'custom-admin/admin_landing_page.html')


def view_admin_all_devices(request):
    if not request.user.is_superuser:
        return HttpResponse('<h1>You are not authorized!</h1>')
    devices = Device.objects.all()
    context = {
        'devices': devices,
    }

    return render(request, 'custom-admin/admin_all_devices.html', context)


def view_admin_all_users(request):
    if not request.user.is_superuser:
        return HttpResponse('<h1>You are not authorized!</h1>')

    users = User.objects.all()

    context = {
        'users': users,
    }

    return render(request, 'custom-admin/admin_all_users.html', context)


def view_admin_current_user_devices(request, pk):
    if not request.user.is_superuser:
        return HttpResponse('<h1>You are not authorized!</h1>')
    devices = Device.objects.filter(user_id=pk)
    context = {
        'devices': devices,
    }

    return render(request, 'custom-admin/admin_all_devices_current_user.html', context)