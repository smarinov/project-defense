from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import RegisterForm, LoginForm, ProfileForm


@login_required
def details_profile(request, pk):
    if request.method == 'GET':
        profile = User.objects.get(pk=pk)
        is_owner = profile.pk == request.user.pk
        is_superuser = request.user.is_superuser
        context = {
            'profile': profile,
            'is_owner': is_owner,
            'is_superuser': is_superuser,
        }
        return render(request, 'accounts/profile.html', context)


def delete_profile(request, pk):
    profile = User.objects.get(pk=pk)
    if request.method == 'GET':
        register_form = RegisterForm(instance=profile)

        context = {
            'profile': profile,
            'register_form': register_form,
        }
        return render(request, 'accounts/delete_profile.html', context)
    else:
        profile.delete()
        return redirect('homepage')


def register_user(request):
    if request.method == 'GET':
        context = {
            'register_form': RegisterForm(),
            'profile_form': ProfileForm(),
        }
        return render(request, 'accounts/register.html', context)
    else:
        register_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if register_form.is_valid() and profile_form.is_valid():
            user = register_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('homepage')
        else:
            context = {
                'register_form': register_form,
                'profile_form': profile_form,
            }
            return render(request, 'accounts/register.html', context)


def login_user(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('homepage')

        context = {
            'login_form': LoginForm(),

        }
        return render(request, 'accounts/login.html', context)
    else:
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('homepage')

        context = {
            'login_form': login_form,
        }

        return render(request, 'accounts/login.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('homepage')
