from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.utils.translation import gettext_lazy as _
from accounts.forms import LoginForm, LoginFormAR, UserCreationForm, UserChangeForm, ChangePasswordFrom
# from accounts.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q


def userRegister(request):
    pass
    # form = RegisterForm()
    # if request.method == 'POST':
    #     form = RegisterForm(request.POST)
    #     if form.is_valid():
    #         cd = form.cleaned_data
    #         if not get_user_model()objects.filter(email=cd['username']).exists():
    #             if not get_user_model()objects.filter(email=cd['email']).exists():
    #                 user = get_user_model()objects.create_user(
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
                if get_user_model().objects.filter(username=cd['username']).exists():
                    user = authenticate(request, username=cd['username'], password=cd['password'])
                    if user is not None:
                        if user.is_superuser or user.is_staff:
                            login(request, user)
                            messages.success(request, _("logged in successfully"), extra_tags="success")
                            return redirect('crm:home')
                        else:
                            messages.success(request, _(
                                "You do not have permission to access this section"), extra_tags="warning")
                            return redirect('accounts:login')
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
    return redirect('accounts:login')


@login_required()
def profile(request):
    user = get_user_model().objects.get(username=request.user.username)
    form = UserChangeForm(request.POST or None, instance=user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, _("updated successfully"), extra_tags="alert alert-success")
            return redirect('accounts:profile')
        else:
            messages.success(request, _("Error updating your profile !!"), extra_tags="warning")
            return redirect('accounts:profile')
    else:
        return render(request, 'crm/obj_update.html', {'form': form})


@login_required()
def profilepass(request):
    if request.user.is_active:
        if request.method == 'POST':
            form = ChangePasswordFrom(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = get_user_model().objects.get(username=request.user.username)
                user.set_password(cd['password1'])
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, _("Your password has been successfully changed"), extra_tags="success")
                return redirect('accounts:login')
        else:
            form = ChangePasswordFrom()
            return render(request, 'crm/obj_update.html', {'form': form})
    else:
        return redirect('crm:home')


@login_required
def overview(request):
    active = get_user_model().objects.filter(is_active=True).count()
    staff = get_user_model().objects.filter(is_staff=True).count()
    superuser = get_user_model().objects.filter(is_superuser=True).count()
    labelsusers = ['Active User', 'Staff User', 'Super User']
    datausers = [active, staff, superuser]

    return render(request, 'accounts/overview.html', {
        'headerTitle': f'User Management Overview',
        'labelsusers': labelsusers,
        'datausers': datausers,
        'totalcount': active+staff+superuser,
    })


class UsersListView(ListView):
    model = get_user_model()
    context_object_name = 'objects'
    template_name = 'accounts/users_list.html'
    paginate_by = 30
    ordering = '-regdate'
    ordering = '-regdate'

    def get_queryset(self):
        queryset = super().get_queryset()
        query_search = self.request.GET.get('q')
        query_filter = self.request.GET.get('f')
        if query_search:
            queryset = queryset.filter(
                Q(username__contains=query_search) |
                Q(phone__contains=query_search) |
                Q(email__contains=query_search)
            )
        if query_filter:
            if query_filter != 'All':
                queryset = queryset.filter(is_active=query_filter)
        return queryset


class UserDetailView(DetailView):
    model = get_user_model()
    context_object_name = 'obj'
    template_name = 'accounts/users_detail.html'


class UserCreateView(CreateView):
    model = get_user_model()
    form_class = UserCreationForm
    template_name = 'crm/obj_create.html'
    success_message = _('Success: Subscription was created.')
    success_url = reverse_lazy('accounts:user_list')


class UsersUpdateView(UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'crm/obj_update.html'
    success_url = reverse_lazy('accounts:user_list')


class UsersUpdatePassView(UpdateView):
    model = get_user_model()
    form_class = ChangePasswordFrom
    template_name = 'crm/obj_update.html'
    success_url = reverse_lazy('accounts:user_list')


class UsersDeleteView(DeleteView):
    model = get_user_model()
    context_object_name = 'obj'
    template_name = 'crm/obj_delete.html'
    success_message = 'Success: Subscription was deleted.'
    success_url = reverse_lazy('accounts:user_list')
