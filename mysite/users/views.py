from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from mysite.settings import EMAIL_HOST_USER
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            form.username = form.cleaned_data['username']
            form.email = form.cleaned_data['email']
            try:
                send_mail(f'New User requests for approval to log in', f'You have a new user and he is awaiting for approve'+'\n\n'+'User name: '+ form.username, form.email, [EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You will be able to log in after Admin approval')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'register': "active" })

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been Updated.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context ={
        'u_form': u_form,
        'p_form': p_form,
        'profile': "active"
    }
    return render(request, 'users/profile.html', context)

@login_required
def profileDetail(request, pk):
    context = {
        'user': get_object_or_404(User, pk=pk)
    }
    return render(request, 'users/user_detail.html', context)