from django.shortcuts import render
from django.views.generic import ListView
from crm.models import Common60
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'crm/home.html')


@login_required
def dashboard(request):
    return render(request, 'crm/dashboard.html')


class C60List(ListView):
    model = Common60
    context_object_name = 'c60list'
    template_name = 'crm/c60_list.html'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        if 'type' in self.request.GET:
            qs = qs.filter(book_type=int(self.request.GET['type']))
        return qs
