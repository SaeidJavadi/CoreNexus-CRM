from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from crm.models import Common60, Common61, Common70
from django.contrib.auth.decorators import login_required
from crm.forms import ObjectModelForm60, ObjectModelForm61, ObjectModelForm70
from django.urls import reverse_lazy


@login_required
def home(request):
    return render(request, 'crm/home.html')


@login_required
def dashboard(request):
    return render(request, 'crm/dashboard.html')


class c60List(ListView):        # Common60
    model = Common60
    context_object_name = 'c60list'
    template_name = 'crm/c60_list.html'
    paginate_by = 30


class C60ReadView(DetailView):
    model = Common60
    context_object_name = 'c60'
    template_name = 'crm/c60_read.html'


class C60CreateView(CreateView):
    model = Common60
    form_class = ObjectModelForm60
    context_object_name = 'c60'
    template_name = 'crm/c60_create.html'
    success_message = 'Success: Subscription was created.'
    success_url = reverse_lazy('crm:c60_list')


class C60EUpdateView(UpdateView):
    model = Common60
    form_class = ObjectModelForm60
    context_object_name = 'c60'
    template_name = 'crm/c60_update.html'
    success_url = reverse_lazy('crm:c60_list')


class C60DeleteView(DeleteView):
    model = Common60
    context_object_name = 'c60'
    template_name = 'crm/c60_delete.html'
    success_message = 'Success: Subscription was deleted.'
    success_url = reverse_lazy('crm:c60_list')


class c61List(ListView):        # Common61
    model = Common61
    context_object_name = 'c60list'
    template_name = 'crm/c60_list.html'
    paginate_by = 30


class C61ReadView(DetailView):
    model = Common61
    context_object_name = 'c60'
    template_name = 'crm/c60_read.html'


class C61CreateView(CreateView):
    model = Common61
    form_class = ObjectModelForm61
    template_name = 'crm/c60_create.html'
    success_message = 'Success: Subscription was created.'
    success_url = reverse_lazy('crm:c61_list')


class C61EUpdateView(UpdateView):
    model = Common61
    form_class = ObjectModelForm61
    context_object_name = 'c60'
    template_name = 'crm/c60_update.html'
    success_message = 'Success: Subscription was updated.'
    success_url = reverse_lazy('crm:c61_list')


class C61DeleteView(DeleteView):
    model = Common61
    context_object_name = 'c60'
    template_name = 'crm/c60_delete.html'
    success_message = 'Success: Subscription was deleted.'
    success_url = reverse_lazy('crm:c61_list')


class c70List(ListView):        # Common61
    model = Common70
    context_object_name = 'c60list'
    template_name = 'crm/c60_list.html'
    paginate_by = 30


class C70ReadView(DetailView):
    model = Common70
    context_object_name = 'c60'
    template_name = 'crm/c60_read.html'


class C70CreateView(CreateView):
    model = Common70
    form_class = ObjectModelForm70
    template_name = 'crm/c60_create.html'
    success_message = 'Success: Subscription was created.'
    success_url = reverse_lazy('crm:c70_list')


class C70EUpdateView(UpdateView):
    model = Common70
    form_class = ObjectModelForm70
    context_object_name = 'c60'
    template_name = 'crm/c60_update.html'
    success_message = 'Success: Subscription was updated.'
    success_url = reverse_lazy('crm:c70_list')


class C70DeleteView(DeleteView):
    model = Common70
    context_object_name = 'c60'
    template_name = 'crm/c60_delete.html'
    success_message = 'Success: Subscription was deleted.'
    success_url = reverse_lazy('crm:c70_list')
