from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from secondtech_app.forms import DeviceForm, SearchForm
from secondtech_app.models import Device
from secondtech_core.decorators import group_required


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
            devices = Device.objects.filter(title__icontains=query)
            context = {
                'devices': devices,
                'form': form,
            }
            return render(request, 'all_devices.html', context)


@login_required
@group_required(groups=['Regular User'])
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
@group_required(groups=['Regular User'])
def delete_device(request, pk):
    device = Device.objects.get(pk=pk)
    if request.user.pk == device.user.pk or request.user.is_superuser:
        if request.method == 'GET':
            context = {
                'device': device,
            }
            return render(request, 'delete_device.html', context)
        else:
            device.delete()
            return redirect('view devices')
    else:
        return redirect('homepage')


@login_required
@group_required(groups=['Regular User'])
def details_device(request, pk):
    device = Device.objects.get(pk=pk)
    is_owner = device.user.id == request.user.id
    is_superuser = request.user.is_superuser
    more_devices_from_this_user = [more_devices for more_devices in Device.objects.filter(user=device.user) if
                                   more_devices != device]
    context = {
        'device': device,
        'is_owner': is_owner,
        'is_superuser': is_superuser,
        'more_devices_from_this_user': more_devices_from_this_user,
    }

    return render(request, 'details_device.html', context)


@login_required
@group_required(groups=['Regular User'])
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
                'device': device,
            }
            return render(request, 'edit_device.html', context)
    else:
        return redirect('details device', pk)


def view_smartphones(request):
    form = SearchForm()
    smartphones = Device.objects.filter(type='Smartphone')
    if request.method == 'GET':
        context = {
            'smartphones': smartphones,
            'form': form,
        }
        return render(request, 'only_smartphones.html', context)
    else:
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['text']
            smartphones = smartphones.filter(title__icontains=query)
            context = {
                'smartphones': smartphones,
                'form': form,
            }
            return render(request, 'only_smartphones.html', context)


def view_tablets(request):
    form = SearchForm()
    tablets = Device.objects.filter(type='Tablet')
    if request.method == 'GET':
        context = {
            'tablets': tablets,
            'form': form,
        }
        return render(request, 'only_tablets.html', context)
    else:
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['text']
            tablets = tablets.filter(title__icontains=query)
            context = {
                'tablets': tablets,
                'form': form,
            }
            return render(request, 'only_tablets.html', context)


def view_laptops(request):
    form = SearchForm()
    laptops = Device.objects.filter(type='Laptop')
    if request.method == 'GET':
        context = {
            'laptops': laptops,
            'form': form,
        }
        return render(request, 'only_laptops.html', context)
    else:
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['text']
            laptops = laptops.filter(title__icontains=query)
            context = {
                'laptops': laptops,
                'form': form,
            }
            return render(request, 'only_laptops.html', context)
