from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from crm.models import Common60, Common61, Common70, CommonDead, JudiciaryDead, DoingDead, PublicAssistance
from django.contrib.auth.decorators import login_required
from crm.forms import ObjectModelForm60, ObjectModelForm61, ObjectModelForm70, ObjectModelFormCd, ObjectModelFormJd, ObjectModelFormDd, ObjectModelFormPa
from django.urls import reverse_lazy


@login_required
def home(request):
    return render(request, 'crm/home.html')


@login_required
def dashboard(request):
    return render(request, 'crm/dashboard.html')


class c60List(ListView):        # Common60
    model = Common60
    context_object_name = 'objects'
    template_name = 'crm/obj_list.html'
    paginate_by = 30


class C60ReadView(DetailView):
    model = Common60
    context_object_name = 'obj'
    template_name = 'crm/obj_read.html'


class C60CreateView(CreateView):
    model = Common60
    form_class = ObjectModelForm60
    template_name = 'crm/obj_create.html'
    success_message = 'Success: Subscription was created.'
    success_url = reverse_lazy('crm:c60_list')


class C60EUpdateView(UpdateView):
    model = Common60
    form_class = ObjectModelForm60
    template_name = 'crm/obj_update.html'
    success_url = reverse_lazy('crm:c60_list')


class C60DeleteView(DeleteView):
    model = Common60
    context_object_name = 'obj'
    template_name = 'crm/obj_delete.html'
    success_message = 'Success: Subscription was deleted.'
    success_url = reverse_lazy('crm:c60_list')


class c61List(ListView):        # Common61
    model = Common61
    context_object_name = 'objects'
    template_name = 'crm/obj_list.html'
    paginate_by = 30


class C61ReadView(DetailView):
    model = Common61
    context_object_name = 'obj'
    template_name = 'crm/obj_read.html'


class C61CreateView(CreateView):
    model = Common61
    form_class = ObjectModelForm61
    template_name = 'crm/obj_create.html'
    success_message = 'Success: Subscription was created.'
    success_url = reverse_lazy('crm:c61_list')


class C61EUpdateView(UpdateView):
    model = Common61
    form_class = ObjectModelForm61
    template_name = 'crm/obj_update.html'
    success_message = 'Success: Subscription was updated.'
    success_url = reverse_lazy('crm:c61_list')


class C61DeleteView(DeleteView):
    model = Common61
    context_object_name = 'obj'
    template_name = 'crm/obj_delete.html'
    success_message = 'Success: Subscription was deleted.'
    success_url = reverse_lazy('crm:c61_list')


class c70List(ListView):        # Common61
    model = Common70
    context_object_name = 'objects'
    template_name = 'crm/obj_list.html'
    paginate_by = 30


class C70ReadView(DetailView):
    model = Common70
    context_object_name = 'obj'
    template_name = 'crm/obj_read.html'


class C70CreateView(CreateView):
    model = Common70
    form_class = ObjectModelForm70
    template_name = 'crm/obj_create.html'
    success_message = 'Success: Subscription was created.'
    success_url = reverse_lazy('crm:c70_list')


class C70EUpdateView(UpdateView):
    model = Common70
    form_class = ObjectModelForm70
    template_name = 'crm/obj_update.html'
    success_message = 'Success: Subscription was updated.'
    success_url = reverse_lazy('crm:c70_list')


class C70DeleteView(DeleteView):
    model = Common70
    context_object_name = 'obj'
    template_name = 'crm/obj_delete.html'
    success_message = 'Success: Subscription was deleted.'
    success_url = reverse_lazy('crm:c70_list')


class CdList(ListView):        # CommonDead
    model = CommonDead
    context_object_name = 'objects'
    template_name = 'crm/cdjd_list.html'
    paginate_by = 30


class CdReadView(DetailView):
    model = CommonDead
    context_object_name = 'obj'
    template_name = 'crm/cdjd_read.html'


class CdCreateView(CreateView):
    model = CommonDead
    form_class = ObjectModelFormCd
    template_name = 'crm/obj_create.html'
    success_message = 'Success: Subscription was created.'
    success_url = reverse_lazy('crm:cd_list')


class CdUpdateView(UpdateView):
    model = CommonDead
    form_class = ObjectModelFormCd
    template_name = 'crm/obj_update.html'
    success_message = 'Success: Subscription was updated.'
    success_url = reverse_lazy('crm:cd_list')


class CdDeleteView(DeleteView):
    model = CommonDead
    context_object_name = 'obj'
    template_name = 'crm/obj_delete.html'
    success_message = 'Success: Subscription was deleted.'
    success_url = reverse_lazy('crm:cd_list')


class JdList(ListView):        # JudiciaryDead
    model = JudiciaryDead
    context_object_name = 'objects'
    template_name = 'crm/cdjd_list.html'
    paginate_by = 30


class JdReadView(DetailView):
    model = JudiciaryDead
    context_object_name = 'obj'
    template_name = 'crm/cdjd_read.html'


class JdCreateView(CreateView):
    model = JudiciaryDead
    form_class = ObjectModelFormJd
    template_name = 'crm/obj_create.html'
    success_message = 'Success: Subscription was created.'
    success_url = reverse_lazy('crm:jd_list')


class JdUpdateView(UpdateView):
    model = JudiciaryDead
    form_class = ObjectModelFormJd
    template_name = 'crm/obj_update.html'
    success_message = 'Success: Subscription was updated.'
    success_url = reverse_lazy('crm:jd_list')


class JdDeleteView(DeleteView):
    model = JudiciaryDead
    context_object_name = 'obj'
    template_name = 'crm/obj_delete.html'
    success_message = 'Success: Subscription was deleted.'
    success_url = reverse_lazy('crm:jd_list')


class DdList(ListView):        # DoingDead
    model = DoingDead
    context_object_name = 'objects'
    template_name = 'crm/dd_list.html'
    paginate_by = 30


class DdReadView(DetailView):
    model = DoingDead
    context_object_name = 'obj'
    template_name = 'crm/dd_read.html'


class DdCreateView(CreateView):
    model = DoingDead
    form_class = ObjectModelFormDd
    template_name = 'crm/obj_create.html'
    success_message = 'Success: Subscription was created.'
    success_url = reverse_lazy('crm:dd_list')


class DdUpdateView(UpdateView):
    model = DoingDead
    form_class = ObjectModelFormDd
    template_name = 'crm/obj_update.html'
    success_message = 'Success: Subscription was updated.'
    success_url = reverse_lazy('crm:dd_list')


class DdDeleteView(DeleteView):
    model = DoingDead
    context_object_name = 'obj'
    template_name = 'crm/obj_delete.html'
    success_message = 'Success: Subscription was deleted.'
    success_url = reverse_lazy('crm:dd_list')


class PaList(ListView):        # PublicAssistance
    model = PublicAssistance
    context_object_name = 'objects'
    template_name = 'crm/pa_list.html'
    paginate_by = 30


class PaReadView(DetailView):
    model = PublicAssistance
    context_object_name = 'obj'
    template_name = 'crm/pa_read.html'


class PaCreateView(CreateView):
    model = PublicAssistance
    form_class = ObjectModelFormPa
    template_name = 'crm/obj_create.html'
    success_message = 'Success: Subscription was created.'
    success_url = reverse_lazy('crm:pa_list')


class PaUpdateView(UpdateView):
    model = PublicAssistance
    form_class = ObjectModelFormPa
    template_name = 'crm/obj_update.html'
    success_message = 'Success: Subscription was updated.'
    success_url = reverse_lazy('crm:pa_list')


class PaDeleteView(DeleteView):
    model = PublicAssistance
    context_object_name = 'obj'
    template_name = 'crm/obj_delete.html'
    success_message = 'Success: Subscription was deleted.'
    success_url = reverse_lazy('crm:pa_list')


class ActiveSubscripe():
    pass
