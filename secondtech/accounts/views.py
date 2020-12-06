from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import RegisterForm, LoginForm, ProfileForm, EditUserForm
from accounts.models import UserProfile


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


@login_required
def delete_profile(request, pk):
    profile = User.objects.get(pk=pk)
    if request.user.pk == profile.pk or request.user.is_superuser:
        if request.method == 'GET':
            context = {
                'profile': profile,
            }
            return render(request, 'accounts/delete_profile.html', context)
        else:
            profile.delete()
            return redirect('homepage')
    else:
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
            if not request.FILES:
                profile.profile_picture = 'profiles/default-profile.jpg'
            profile.save()

            login(request, user)
            return redirect('homepage')
        else:
            context = {
                'register_form': register_form,
                'profile_form': profile_form,
            }
            return render(request, 'accounts/register.html', context)


@login_required
def edit_profile(request, pk):
    current_user = User.objects.get(pk=pk)
    current_profile = UserProfile.objects.get(user=current_user)
    if request.user.id == current_user.id or request.user.is_superuser:
        if request.method == 'GET':
            user_form = EditUserForm(instance=current_user)
            profile_form = ProfileForm(instance=current_profile)

            context = {
                'user_form': user_form,
                'profile_form': profile_form,
                'user': current_user,
                'current_profile': current_profile,
            }
            return render(request, 'accounts/edit_profile.html', context)
        else:
            user_form = EditUserForm(request.POST, instance=current_user)
            profile_form = ProfileForm(request.POST, request.FILES, instance=current_profile)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                return redirect('user profile', current_user.id)
            context = {
                'user_form': user_form,
                'profile_form': profile_form,
                'user': current_user,
                'current_profile': current_profile,
            }
            return render(request, 'accounts/edit_profile.html', context)
    else:
        return redirect('homepage')


@login_required
def change_password(request, pk):
    current_user = User.objects.get(pk=pk)
    if request.user.id == current_user.id or request.user.is_superuser:
        password_form = PasswordChangeForm(user=current_user)
        if request.method == 'GET':
            context = {
                'password_form': password_form,
            }
            return render(request, 'accounts/change_password.html', context)
        else:
            password_form = PasswordChangeForm(data=request.POST, user=current_user)
            if password_form.is_valid():
                password_form.save()
                update_session_auth_hash(request, password_form.user)
                return redirect('user profile', current_user.pk)
            else:
                context = {
                    'password_form': password_form,
                }
                return render(request, 'accounts/change_password.html', context)
    else:
        return redirect('homepage')


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
