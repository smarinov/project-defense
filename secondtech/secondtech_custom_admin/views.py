from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accounts.models import Comment
from secondtech_app.models import Device


def view_admin_landing_page(request):
    if not request.user.is_superuser:
        return HttpResponse('<h1>You are not authorized!</h1>')
    return render(request, 'custom-admin/admin_landing_page.html')


def view_admin_all_devices(request):
    if not request.user.is_superuser:
        return HttpResponse('<h1>You are not authorized!</h1>')
    devices = Device.objects.all().order_by('-id')
    context = {
        'devices': devices,
    }

    return render(request, 'custom-admin/admin_all_devices.html', context)


def view_admin_all_users(request):
    if not request.user.is_superuser:
        return HttpResponse('<h1>You are not authorized!</h1>')

    users = User.objects.all().order_by('-id')

    context = {
        'users': users,
    }

    return render(request, 'custom-admin/admin_all_users.html', context)


def view_admin_current_user_devices(request, pk):
    if not request.user.is_superuser:
        return HttpResponse('<h1>You are not authorized!</h1>')
    devices = Device.objects.filter(user_id=pk).order_by('-id')
    context = {
        'devices': devices,
    }

    return render(request, 'custom-admin/admin_all_devices_current_user.html', context)


def view_admin_all_comments(request):
    if not request.user.is_superuser:
        return HttpResponse('<h1>You are not authorized!</h1>')
    comments = Comment.objects.all().order_by('-id')
    context = {
        'comments': comments,
    }

    return render(request, 'custom-admin/admin_all_comments.html', context)


def view_admin_comment(request, pk):
    if not request.user.is_superuser:
        return HttpResponse('<h1>You are not authorized!</h1>')
    comment = Comment.objects.get(pk=pk)
    context = {
        'comment': comment,
    }
    return render(request, 'custom-admin/admin_view_comment.html', context)