from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)
from crm.forms import (
    ObjModelForm,
    ObjFilterForm
)
from crm.models import Book


@login_required
def home(request):
    return render(request, 'crm/home.html')


@login_required
def dashboard(request):
    return render(request, 'crm/dashboard.html')


class C60List(generic.ListView):
    model = Book
    context_object_name = 'objs'
    template_name = 'crm/c60_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        if 'type' in self.request.GET:
            qs = qs.filter(book_type=int(self.request.GET['type']))
        return qs


class ObjFilterView(BSModalFormView):
    template_name = 'curd/filter_obj.html'
    form_class = ObjFilterForm

    def form_valid(self, form):
        self.filter = '?type=' + form.cleaned_data['type']
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('crm:c60list') + self.filter


class ObjCreateView(BSModalCreateView):
    template_name = 'curd/create_obj.html'
    form_class = ObjModelForm
    success_message = 'Success: Obj was created.'
    success_url = reverse_lazy('crm:c60list')


class ObjUpdateView(BSModalUpdateView):
    model = Book
    context_object_name = 'obj'
    template_name = 'curd/update_obj.html'
    form_class = ObjModelForm
    success_message = 'Success: Obj was updated.'
    success_url = reverse_lazy('crm:c60list')


class ObjReadView(BSModalReadView):
    model = Book
    context_object_name = 'obj'
    template_name = 'curd/read_obj.html'


class ObjDeleteView(BSModalDeleteView):
    model = Book
    context_object_name = 'obj'
    template_name = 'curd/delete_obj.html'
    success_message = 'Success: Obj was deleted.'
    success_url = reverse_lazy('crm:c60list')


# @login_required()
def objs(request):
    data = {}
    if request.method == 'GET':
        objs = Book.objects.all()
        data['table'] = render_to_string(
            'crm/_objs_table.html',
            {'objs': objs},
            request=request
        )
        return JsonResponse(data)
