from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, View, DeleteView
from crm.models import Common60


@login_required
def home(request):
    return render(request, 'crm/home.html')


@login_required
def dashboard(request):
    return render(request, 'crm/dashboard.html')


class C60sListView(TemplateView):
    template_name = "crm/c60_list.html"
    context_object_name = "commons"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Common60.objects.all()
        return context


class CreateCrudUser(View):
    def get(self, request):
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = Common60.objects.create(
            name=name1,
            address=address1,
            age=age1
        )

        user = {'id': obj.id, 'name': obj.name, 'address': obj.address, 'age': obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)


class DeleteCrudUser(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Common60.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class UpdateCrudUser(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = Common60.objects.get(id=id1)
        obj.name = name1
        obj.address = address1
        obj.age = age1
        obj.save()

        user = {'id': obj.id, 'name': obj.name, 'address': obj.address, 'age': obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)
