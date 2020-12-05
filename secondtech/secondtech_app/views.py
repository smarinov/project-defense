from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from secondtech_app.forms import DeviceForm, SearchForm
from secondtech_app.models import Device


def homepage(request):
    return render(request, 'landing_page.html')


def about_page(request):
    return render(request, 'about_us.html')


def view_devices(request):
    form = SearchForm()
    devices = Device.objects.all()
    if request.method == 'GET':
        context = {
            'devices': devices,
            'form': form,
        }
        return render(request, 'all_devices.html', context)
    else:
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['text']
            devices = Device.objects.filter(title__contains=query)
            context = {
                'devices': devices,
                'form': form,
            }
            return render(request, 'all_devices.html', context)


@login_required
def add_device(request):
    if request.method == 'GET':
        context = {
            'form': DeviceForm()
        }

        return render(request, 'add_device.html', context)
    else:
        form = DeviceForm(request.POST, request.FILES)
        if form.is_valid():
            device = form.save(commit=False)
            device.user = request.user
            device.save()
            return redirect('view devices')
        else:
            context = {
                'form': form
            }

            return render(request, 'add_device.html', context)


@login_required
def delete_device(request, pk):
    device = Device.objects.get(pk=pk)
    if request.user.pk == device.user.pk:
        if request.method == 'GET':
            context = {
                'device': device,
            }
            return render(request, 'delete_device.html', context)
        else:
            device.delete()
            return redirect('homepage')
    else:
        return redirect('homepage')


@login_required
def details_device(request, pk):
    device = Device.objects.get(pk=pk)
    is_owner = device.user.id == request.user.id
    is_superuser = request.user.is_superuser
    format_price = f"{device.price:.2f}"
    context = {
        'device': device,
        'format_price': format_price,
        'is_owner': is_owner,
        'is_superuser': is_superuser,
    }

    return render(request, 'details_device.html', context)


@login_required
def edit_device(request, pk):
    device = Device.objects.get(pk=pk)
    if request.user.pk == device.user.pk or request.user.is_superuser:
        if request.method == 'GET':
            form = DeviceForm(instance=device)
            context = {
                'device': device,
                'form': form,
            }
            return render(request, 'edit_device.html', context)
        else:
            form = DeviceForm(request.POST, instance=device)
            if form.is_valid():
                form.save()
                return redirect('details device', pk)
            context = {
                'form': form,
            }
            return render(request, 'edit_device.html', context)
    else:
        return redirect('details device', pk)
