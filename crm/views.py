from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from crm.models import Common60, Common61, Common70, CommonDead, JudiciaryDead, DoingDead, PublicAssistance, Lottery, Notification, WinnerLottery60
from django.contrib.auth.decorators import login_required
from crm.forms import ObjectModelForm60, ObjectModelForm61, ObjectModelForm70, ObjectModelFormCd, ObjectModelFormJd, ObjectModelFormDd, ObjectModelFormPa, ObjectModelFormMSG, HodlingLotteryForm
from accounts.models import User
from django.urls import reverse_lazy
from django.utils import timezone
from datetime import datetime
from django.db.models import Sum
from django.http import HttpResponse
from crm.tasks import send_notification
from django.db.models import Q
import random


@login_required
def home(request):
    return render(request, 'crm/home.html')


def assetlinks(request):
    json_content = [{
        "relation": ["delegate_permission/common.handle_all_urls"],
        "target": {
            "namespace": "android_app",
            "package_name": "com.social.solidarity",
            "sha256_cert_fingerprints":
            ["98:77:4A:24:31:CD:40:05:24:86:9D:6D:CD:58:2D:12:B9:79:1C:E2:E6:2E:E9:CB:51:0F:EA:96:DE:36:A3:75"]
        }
    }]
    return HttpResponse(
        json_content,
        content_type='application/json',
        status=200
    )


@login_required
def sendemailtest(request):
    from django.core.mail import send_mail
    a = send_mail(
        'Subject',  # email subject
        'Message body',  # email body
        'social.solidarity2023@gmail.com',  # sender's email address
        ['7saeid2@gmail.com'],  # list of recipient email addresses
        fail_silently=False,  # set to True to suppress exceptions
    )
    return HttpResponse(a)


@login_required
def dashboard(request):
    return render(request, 'crm/dashboard.html')


@login_required
def overview(request, model):
    if model == 'c60':
        MODEL = Common60
        TiTle = "0-60"
    elif model == 'c61':
        MODEL = Common61
        TiTle = "61-69"
    elif model == 'c70':
        MODEL = Common70
        TiTle = "70-up"
    elif model == 'cd':
        MODEL = CommonDead
        TiTle = "Subscription Dead"
    elif model == 'jd':
        MODEL = JudiciaryDead
        TiTle = "Judiciary Dead"
    elif model == 'dd':
        MODEL = DoingDead
        TiTle = "Doing Dead"
    elif model == 'pa':
        MODEL = PublicAssistance
        TiTle = "Public Assistance"
    # Amount Month Chart
    today = datetime.now(tz=timezone.utc)
    year = today.year
    month = today.month
    labelsamount = []
    dataamount = []
    totalamount = MODEL.objects.filter(status=True).aggregate(total=Sum('amount'))['total']
    for i in range(1, 13):
        labelsamount.append(f'{year}-{month}')
        objmonth = MODEL.objects.filter(status=True, create__year=year, create__month=month)
        amountCount = 0
        for obj in objmonth:
            amountCount += obj.amount
        dataamount.append(amountCount)
        print('='*30)
        print(f'{year}-{month}', f'= {amountCount} -> len={objmonth.count()}')
        print('='*30)
        if month == 1:
            year -= 1
            month = 12
        month -= 1
        print("="*30)
    print(dataamount, len(dataamount))
    print("="*30)
    print(labelsamount, len(labelsamount))
    print("="*30)
    print(totalamount)

    spay = MODEL.objects.filter(status=True).count()
    unspay = MODEL.objects.filter(status=False).count()

    if model != 'pa':
        Iraq = MODEL.objects.filter(contery='Iraq').count()
        Iran = MODEL.objects.filter(contery='Iran').count()
        Syria = MODEL.objects.filter(contery='Syria').count()
        Sweden = MODEL.objects.filter(contery='Sweden').count()
        Australia = MODEL.objects.filter(contery='Australia').count()
        Denmark = MODEL.objects.filter(contery='Denmark').count()
        Lebanon = MODEL.objects.filter(contery='Lebanon').count()
        SaudiArabia = MODEL.objects.filter(contery='SaudiArabia').count()
        Bahrain = MODEL.objects.filter(contery='Bahrain').count()
        Kuwait = MODEL.objects.filter(contery='Kuwait').count()
        Emirates = MODEL.objects.filter(contery='Emirates').count()
        America = MODEL.objects.filter(contery='America').count()
        India = MODEL.objects.filter(contery='India').count()
        Pakistan = MODEL.objects.filter(contery='Pakistan').count()
        Turkiye = MODEL.objects.filter(contery='Turkiye').count()

    labelspay = ['Successful Payments', 'Unsuccessful Payments']
    datapay = [spay, unspay]
    if model != 'pa':
        labelscontery = ['Iraq', 'Iran', 'Syria', 'Sweden', 'Australia', 'Denmark', 'Lebanon',
                         'SaudiArabia', 'Bahrain', 'Kuwait', 'Emirates', 'America', 'India', 'Pakistan', 'Turkiye']
        datacontery = [Iraq, Iran, Syria, Sweden, Australia, Denmark, Lebanon,
                       SaudiArabia, Bahrain, Kuwait, Emirates, America, India, Pakistan, Turkiye]
        total = 0
        for item in datacontery:
            if str(item).isdigit():
                total += item
    else:
        datacontery = None
        labelscontery = None
        total = None

    return render(request, 'crm/overview.html', {
        'headerTitle': f'Subscription {TiTle} Overview',
        'labelspay': labelspay,
        'datapay': datapay,
        'totalcount': spay+unspay,
        'totalcountery': total,
        'datacontery': datacontery,
        'labelscontery': labelscontery,
        'dataamount': dataamount,
        'labelsamount': labelsamount,
        'totalamount': totalamount
    })


class c60List(ListView):        # Common60
    model = Common60
    context_object_name = 'objects'
    template_name = 'crm/obj_list.html'
    paginate_by = 30
    ordering = ('-create',)

    def get_queryset(self):
        queryset = super().get_queryset()
        query_search = self.request.GET.get('q')
        query_filter = self.request.GET.get('f')
        if query_search:
            queryset = queryset.filter(
                Q(name__contains=query_search) |
                Q(idcode__contains=query_search) |
                Q(phone__contains=query_search) |
                Q(usersubmit__username__contains=query_search) |
                Q(contery__contains=query_search) |
                Q(city__contains=query_search)
            )
        if query_filter:
            if query_filter != 'All':
                queryset = queryset.filter(status=query_filter)
        return queryset


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


class LotteryListView(ListView):
    model = Common60
    context_object_name = 'objects'
    template_name = 'crm/obj_list.html'
    paginate_by = 30
    ordering = ('-create',)

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.kwargs.get('title')
        query_search = self.request.GET.get('q')
        query_filter = self.request.GET.get('f')
        if title:
            lot = Lottery.objects.get(title=title)
            queryset = super().get_queryset().filter(lottery=lot)
        if query_search:
            queryset = queryset.filter(
                Q(name__contains=query_search) |
                Q(idcode__contains=query_search) |
                Q(phone__contains=query_search) |
                Q(usersubmit__username__contains=query_search) |
                Q(contery__contains=query_search) |
                Q(city__contains=query_search)
            )
        if query_filter:
            if query_filter != 'All':
                queryset = queryset.filter(status=query_filter)
        return queryset


@login_required
def HoldingLottery(request, title):
    form = HodlingLotteryForm()
    if request.method == 'POST':
        form = HodlingLotteryForm(request.POST)
        if form.is_valid():
            nameform = form.cleaned_data['name']
            winner_count = form.cleaned_data['countwinner']
            winstatus = form.cleaned_data['winstatus']
            lot = Lottery.objects.get(title=title)
            try:
                commons = Common60.objects.filter(lottery=lot).values_list('id')
                commons_count = commons.count()
            except:
                commons_count = 0
            if commons_count > 0:
                list_lot = tuple([i[0] for i in commons])
                user_winner = random.sample(list_lot, winner_count)
                for id in user_winner:
                    cw = Common60.objects.get(id=id)
                    w = WinnerLottery60.objects.create(name=nameform, lottery=lot, common=cw)
                    send_notification(user_token=cw.usersubmit.fcmtoken,
                                      title="Lottery Win", body="You have won the lottery")
                    print("="*30)
                    print(f"{nameform} {winner_count} {winstatus}")
                    print("="*30)
                    if winstatus:
                        cw.lottery = None
                        cw.save()
                return redirect('crm:c60_drawdetail', name=str(nameform))
            else:
                return HttpResponse("None List")
    else:
        return render(request, 'crm/obj_create.html', {'form': form})


@login_required
def DrawsLottery(request, title):
    if title == "quran" or title == "ziarat":
        lot = Lottery.objects.get(title=title)
        winner_list = WinnerLottery60.objects.all().values_list('name', 'windate').filter(lottery=lot).distinct()
        return render(request, 'crm/lottery_draws.html', {'draws': winner_list})
    else:
        return HttpResponse("404")


@login_required()
def DrawsDetailLottery(request, name):
    if name:
        winner_list = WinnerLottery60.objects.filter(name=name)
        objs = []
        for winners in winner_list:
            objs.append(winners.common)
        return render(request, 'crm/lottery_drawsdetail.html', {'objects': objs})
    else:
        return HttpResponse("404")


class c61List(ListView):        # Common61
    model = Common61
    context_object_name = 'objects'
    template_name = 'crm/obj_list.html'
    paginate_by = 30
    ordering = ('-create',)

    def get_queryset(self):
        queryset = super().get_queryset()
        query_search = self.request.GET.get('q')
        query_filter = self.request.GET.get('f')
        if query_search:
            queryset = queryset.filter(
                Q(name__contains=query_search) |
                Q(idcode__contains=query_search) |
                Q(phone__contains=query_search) |
                Q(usersubmit__username__contains=query_search) |
                Q(contery__contains=query_search) |
                Q(city__contains=query_search)
            )
        if query_filter:
            if query_filter != 'All':
                queryset = queryset.filter(status=query_filter)
        return queryset


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
    ordering = ('-create',)

    def get_queryset(self):
        queryset = super().get_queryset()
        query_search = self.request.GET.get('q')
        query_filter = self.request.GET.get('f')
        if query_search:
            queryset = queryset.filter(
                Q(name__contains=query_search) |
                Q(idcode__contains=query_search) |
                Q(phone__contains=query_search) |
                Q(usersubmit__username__contains=query_search) |
                Q(contery__contains=query_search) |
                Q(city__contains=query_search)
            )
        if query_filter:
            if query_filter != 'All':
                queryset = queryset.filter(status=query_filter)
        return queryset


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
    ordering = ('-create',)

    def get_queryset(self):
        queryset = super().get_queryset()
        query_search = self.request.GET.get('q')
        query_filter = self.request.GET.get('f')
        if query_search:
            queryset = queryset.filter(
                Q(name__contains=query_search) |
                Q(idcode__contains=query_search) |
                Q(phone__contains=query_search) |
                Q(usersubmit__username__contains=query_search) |
                Q(contery__contains=query_search) |
                Q(city__contains=query_search)
            )
        if query_filter:
            if query_filter != 'All':
                queryset = queryset.filter(status=query_filter)
        return queryset


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
    ordering = ('-create',)

    def get_queryset(self):
        queryset = super().get_queryset()
        query_search = self.request.GET.get('q')
        query_filter = self.request.GET.get('f')
        if query_search:
            queryset = queryset.filter(
                Q(name__contains=query_search) |
                Q(idcode__contains=query_search) |
                Q(phone__contains=query_search) |
                Q(contery__contains=query_search) |
                Q(city__contains=query_search) |
                Q(usersubmit__username__contains=query_search)
            )
        if query_filter:
            if query_filter != 'All':
                queryset = queryset.filter(status=query_filter)
        return queryset


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
    ordering = ('-create',)

    def get_queryset(self):
        queryset = super().get_queryset()
        query_search = self.request.GET.get('q')
        query_filter = self.request.GET.get('f')
        if query_search:
            queryset = queryset.filter(
                Q(name__contains=query_search) |
                Q(phone__contains=query_search) |
                Q(agent__contains=query_search) |
                Q(contery__contains=query_search) |
                Q(city__contains=query_search) |
                Q(usersubmit__username__contains=query_search)
            )
        if query_filter:
            if query_filter != 'All':
                queryset = queryset.filter(status=query_filter)
        return queryset


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
    ordering = ('-create',)

    def get_queryset(self):
        queryset = super().get_queryset()
        query_search = self.request.GET.get('q')
        query_filter = self.request.GET.get('f')
        if query_search:
            queryset = queryset.filter(
                Q(name__contains=query_search) |
                Q(usersubmit__username__contains=query_search)
            )
        if query_filter:
            if query_filter != 'All':
                queryset = queryset.filter(status=query_filter)
        return queryset


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


class ActiveSubscripe(ListView):
    pass


class MessagesListView(ListView):   # Notification Messages
    model = Notification
    context_object_name = 'objects'
    template_name = 'crm/msg_list.html'
    paginate_by = 30
    ordering = ('-createdate',)

    def get_queryset(self):
        queryset = super().get_queryset()
        query_search = self.request.GET.get('q')
        query_filter = self.request.GET.get('f')
        if query_search:
            queryset = queryset.filter(
                Q(name__contains=query_search) |
                Q(idcode__contains=query_search) |
                Q(phone__contains=query_search)
            )
        if query_filter:
            if query_filter != 'All':
                queryset = queryset.filter(status=query_filter)
        return queryset


class MessagesCreateView(CreateView):
    model = Notification
    form_class = ObjectModelFormMSG
    template_name = 'crm/obj_create.html'
    success_message = 'Success: Messege Send.'
    success_url = reverse_lazy('crm:msg_list')

    def form_valid(self, form):
        userselected = form.cleaned_data['user']
        subject = form.cleaned_data['subject']
        text = form.cleaned_data['text']
        for user in userselected:
            print(user)
            fcmtoken = User.objects.get(username=user).fcmtoken
            if fcmtoken != None:
                send_notification(user_token=fcmtoken, title=subject, body=text)
        return super().form_valid(form)


class MessagesDetailView(DetailView):
    model = Notification
    context_object_name = 'obj'
    template_name = 'crm/msg_detail.html'


class MessagesUpdateView(UpdateView):
    model = Notification
    form_class = ObjectModelFormMSG
    template_name = 'crm/obj_update.html'
    success_message = 'Success: Message was updated.'
    success_url = reverse_lazy('crm:msg_list')


class MessagesDeleteView(DeleteView):
    model = Notification
    context_object_name = 'obj'
    template_name = 'crm/obj_delete.html'
    success_message = 'Success: Message was deleted.'
    success_url = reverse_lazy('crm:msg_list')


class MessagesUserCreateView(CreateView):
    model = Notification
    form_class = ObjectModelFormMSG
    template_name = 'crm/obj_create.html'
    success_message = 'Success: Messege Send.'
    success_url = reverse_lazy('crm:msg_list')

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = User.objects.get(pk=self.kwargs.get('pk'))
        return initial
