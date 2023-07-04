from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from accounts.forms import LoginForm, LoginFormAR
# from accounts.forms import RegisterForm
from django.contrib import messages
from accounts.models import User


def userRegister(request):
    pass
    # form = RegisterForm()
    # if request.method == 'POST':
    #     form = RegisterForm(request.POST)
    #     if form.is_valid():
    #         cd = form.cleaned_data
    #         if not User.objects.filter(email=cd['username']).exists():
    #             if not User.objects.filter(email=cd['email']).exists():
    #                 user = User.objects.create_user(
    #                     username=cd['username'], phone=cd['phone'], email=cd['email'], password=cd['password1'])
    #                 user.save()
    #                 login(request, user)
    #                 messages.success(request, _("You successfully registered a user"), extra_tags="success")
    #                 return redirect('crm:home')
    #             else:
    #                 messages.error(request, _("This Email is exists"), extra_tags="warning")
    #         else:
    #             messages.error(request, _("This Username is exists"), extra_tags="warning")
    #     else:
    #         import json
    #         er = json.loads(form.errors.as_json())
    #         for e in er:
    #             messages.error(request, er[e][0]['message'], 'warning')
    # return render(request, 'accounts/register.html', {'form': form})


def userLogin(request):
    if not request.user.is_active:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            formAR = LoginFormAR(request.POST)
            if formAR.is_valid():
                form = formAR
            if form.is_valid():
                cd = form.cleaned_data
                if User.objects.filter(username=cd['username']).exists():
                    user = authenticate(request, username=cd['username'], password=cd['password'])
                    if user is not None:
                        login(request, user)
                        messages.success(request, _("logged in successfully"), extra_tags="success")
                        return redirect('crm:home')
                    else:
                        messages.error(request, _("your username Or Password is wrong"), extra_tags="warning")
                else:
                    messages.error(request, _("No account created with this username"), extra_tags="warning")
                    return redirect('accounts:login')
            else:
                messages.error(request, _("Please enter your information correctly"), extra_tags="warning")
        else:
            form = LoginForm()
            formAR = LoginFormAR()
        return render(request, 'accounts/signinup.html', {'form': form, 'formar': formAR})
    else:
        return redirect('crm:home')


@login_required()
def LogoutPage(request):
    logout(request)
    messages.success(request, _("You Logged Out successfully"), extra_tags="success")
    return redirect('crm:home')
