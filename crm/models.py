from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from accounts.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Common60(models.Model):   # Eshterak afrad 60 saal va kamtar
    usersubmit = models.ForeignKey(User, on_delete=models.CASCADE,
                                   verbose_name=_('Registrant'), related_name='user_c60')
    lottery = models.ForeignKey('lottery', verbose_name=_(
        'lottery'), on_delete=models.SET_NULL, default=None, null=True, blank=True, related_name='lottery_c60')
    name = models.CharField(max_length=120, verbose_name=_('Quadruple common name'))
    age = models.DateField(verbose_name=_('Age'))
    idcode = models.IntegerField(verbose_name=_('Id Code'))
    sickness = models.CharField(verbose_name=_('sickness'), max_length=120)
    contery = models.CharField(verbose_name=_('Contery'), max_length=120)
    city = models.CharField(verbose_name=_('State/City'), max_length=120)
    create = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    phone = models.CharField(verbose_name=_('Phone Number'), max_length=50)
    phoneagent = models.CharField(verbose_name=_('Phone Number Agent'), max_length=50)
    amount = models.FloatField(verbose_name=_('Amount'), blank=True, null=True)
    link = models.TextField(verbose_name=_('Payment Link'), blank=True, null=True)
    status = models.BooleanField(verbose_name=_('Status'), default=False)

    class Meta:
        verbose_name = _('Common60')
        verbose_name_plural = _('Common60s')

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('Common60_detail', kwargs={'pk': self.pk})


class Common61(models.Model):  # Eshterak afrad az 61 ta 69
    usersubmit = models.ForeignKey(User, on_delete=models.CASCADE,
                                   verbose_name=_('Registrant'), related_name='user_c61')
    name = models.CharField(max_length=120, verbose_name=_('Quadruple common name'))
    age = models.DateField(verbose_name=_('Age'))
    idcode = models.IntegerField(verbose_name=_('Id Code'))
    sickness = models.CharField(verbose_name=_('sickness'), max_length=120)
    contery = models.CharField(verbose_name=_('Contery'), max_length=120)
    city = models.CharField(verbose_name=_('State/City'), max_length=120)
    create = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    phone = models.CharField(verbose_name=_('Phone Number'), max_length=50)
    phoneagent = models.CharField(verbose_name=_('Phone Number Agent'), max_length=50)
    amount = models.FloatField(verbose_name=_('Amount'), blank=True, null=True)
    link = models.TextField(verbose_name=_('Payment Link'), blank=True, null=True)
    status = models.BooleanField(verbose_name=_('Status'), default=False)

    class Meta:
        verbose_name = _('Common61')
        verbose_name_plural = _('Common61s')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Common61_detail', kwargs={'pk': self.pk})


class Common70(models.Model):   # Eshterak afrad az 70 salegi va afrad mobtala be bimarihaie jedi
    usersubmit = models.ForeignKey(User, on_delete=models.CASCADE,
                                   verbose_name=_('Registrant'), related_name='user_c70')
    name = models.CharField(max_length=120, verbose_name=_('Quadruple common name'))
    age = models.DateField(verbose_name=_('Age'))
    idcode = models.IntegerField(verbose_name=_('Id Code'))
    sickness = models.CharField(verbose_name=_('sickness'), max_length=120)
    contery = models.CharField(verbose_name=_('Contery'), max_length=120)
    city = models.CharField(verbose_name=_('State/City'), max_length=120)
    create = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    phone = models.CharField(verbose_name=_('Phone Number'), max_length=50)
    phoneagent = models.CharField(verbose_name=_('Phone Number Agent'), max_length=50)
    amount = models.FloatField(verbose_name=_('Amount'), blank=True, null=True)
    link = models.TextField(verbose_name=_('Payment Link'), blank=True, null=True)
    status = models.BooleanField(verbose_name=_('Status'), default=False)

    class Meta:
        verbose_name = _('Common70')
        verbose_name_plural = _('Common70s')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Common70_detail', kwargs={'pk': self.pk})


class CommonDead(models.Model):  # Eshterak FotShodegan
    usersubmit = models.ForeignKey(User, on_delete=models.CASCADE,
                                   verbose_name=_('Registrant'), related_name='user_cd')
    name = models.CharField(max_length=120, verbose_name=_('Deceased name'))
    idcode = models.IntegerField(verbose_name=_('Id Code'))
    contery = models.CharField(verbose_name=_('Contery'), max_length=120)
    city = models.CharField(verbose_name=_('State/City'), max_length=120)
    create = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    phone = models.CharField(verbose_name=_('Phone Number'), max_length=50)
    phoneagent = models.CharField(verbose_name=_('Phone Number Agent'), max_length=50)
    amount = models.FloatField(verbose_name=_('Amount'), blank=True, null=True)
    link = models.TextField(verbose_name=_('Payment Link'), blank=True, null=True)
    status = models.BooleanField(verbose_name=_('Status'), default=False)

    class Meta:
        verbose_name = _('CommonDead')
        verbose_name_plural = _('CommonDeads')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('CommonDead_detail', kwargs={'pk': self.pk})


class JudiciaryDead(models.Model):  # Goveh Ghazaie Mordegan
    usersubmit = models.ForeignKey(User, on_delete=models.CASCADE,
                                   verbose_name=_('Registrant'), related_name='user_jd')
    name = models.CharField(max_length=120, verbose_name=_('Deceased name'))
    idcode = models.IntegerField(verbose_name=_('Id Code'))
    contery = models.CharField(verbose_name=_('Contery'), max_length=120)
    city = models.CharField(verbose_name=_('State/City'), max_length=120)
    create = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    phone = models.CharField(verbose_name=_('Phone Number'), max_length=50)
    phoneagent = models.CharField(verbose_name=_('Phone Number Agent'), max_length=50)
    amount = models.FloatField(verbose_name=_('Amount'), blank=True, null=True)
    link = models.TextField(verbose_name=_('Payment Link'), blank=True, null=True)
    status = models.BooleanField(verbose_name=_('Status'), default=False)

    class Meta:
        verbose_name = _('JudiciaryDead')
        verbose_name_plural = _('JudiciaryDeads')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('JudiciaryDead_detail', kwargs={'pk': self.pk})


class DoingDead(models.Model):  # Anjam Amale Ebadie Marhom
    usersubmit = models.ForeignKey(User, on_delete=models.CASCADE,
                                   verbose_name=_('Registrant'), related_name='user_dd')
    name = models.CharField(max_length=120, verbose_name=_('Deceased name'))
    amount = models.FloatField(verbose_name=_('Amount'), blank=True, null=True)
    yearprayer = models.IntegerField(verbose_name=_('Years Passed prayer'))
    yearfasting = models.IntegerField(verbose_name=_('Years Passed fasting'))
    pilgrimage = models.CharField(max_length=200, verbose_name=_('Pilgrimage'))
    agent = models.CharField(max_length=200, verbose_name=_('Agent'))
    phone = models.CharField(verbose_name=_('Phone Number'), max_length=50)
    contery = models.CharField(verbose_name=_('Contery'), max_length=120)
    city = models.CharField(verbose_name=_('State/City'), max_length=120)
    deposit = models.FloatField(verbose_name=_('Deposit'))
    create = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    link = models.TextField(verbose_name=_('Payment Link'), blank=True, null=True)
    status = models.BooleanField(verbose_name=_('Status'), default=False)

    class Meta:
        verbose_name = _('DoingDead')
        verbose_name_plural = _('DoingDeads')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('DoingDead_detail', kwargs={'pk': self.pk})


class PublicAssistance(models.Model):  # komak be khirieh
    usersubmit = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Registrant'), related_name='user_pa')
    name = models.CharField(max_length=150, verbose_name=_('Deceased name'))
    help_name = models.CharField(max_length=120, verbose_name=_('help name'))
    create = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    amount = models.FloatField(verbose_name=_('amount'))
    link = models.TextField(verbose_name=_('Payment Link'), blank=True, null=True)
    status = models.BooleanField(verbose_name=_('Status'), default=False)

    class Meta:
        verbose_name = _('PublicAssistance')
        verbose_name_plural = _('PublicAssistances')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('PublicAssistance_detail', kwargs={'pk': self.pk})


class Lottery(models.Model):
    lottery_field = (
        ('quran', _('Quran memorization lottery')),
        ('ziarat', _('Visiting religious places'))
    )
    title = models.CharField(max_length=200, verbose_name=_('Lottery'), choices=lottery_field, blank=True, null=True)

    class Meta:
        verbose_name = _('Lottery')
        verbose_name_plural = _('Lotterys')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Lottery_detail', kwargs={'pk': self.pk})


class WinnerLottery60(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('Name'))
    common = models.ForeignKey('Common60', on_delete=models.CASCADE, related_name='winquran')
    lottery = models.ForeignKey('lottery',  on_delete=models.CASCADE, related_name='winlottery')
    windate = models.DateTimeField(verbose_name=_('Add Time'), auto_now=True)

    class Meta:
        verbose_name = _('WinnerLottery60')
        verbose_name_plural = _('WinnerLottery60s')
        # unique_together = ('name', 'windate')

    def __str__(self):
        return str(self.name)+'_'+str(self.windate)

    def get_absolute_url(self):
        return reverse('WinnerLottery60_detail', kwargs={'pk': self.pk})


class Notification(models.Model):
    user = models.ManyToManyField(User, verbose_name=_('User'), related_name='user_msg')
    createdate = models.DateTimeField(auto_now_add=True, verbose_name=_('Create Date'))
    seedate = models.DateTimeField(auto_now=True, verbose_name=_('See Date'))
    subject = models.CharField(verbose_name=_('Subject'), max_length=120)
    text = models.TextField(verbose_name=_('Text'))
    see = models.JSONField(verbose_name=_('See'), default={})

    class Meta:
        verbose_name = _('Notification')
        verbose_name_plural = _('Notifications')

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('Notification_detail', kwargs={'pk': self.pk})


class TableName(models.Model):
    name = models.CharField(verbose_name=_('Table Name'), max_length=150)
    footer = models.CharField(verbose_name=_('Footer'), max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = _("TableName")
        verbose_name_plural = _("TableNames")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("TableName_detail", kwargs={"pk": self.pk})


class TableGift(models.Model):
    tablename = models.ForeignKey(TableName(), verbose_name=_("Table Name"),
                                  on_delete=models.CASCADE, related_name='tabgift')
    monthnumber = models.FloatField(verbose_name=_('Month Number'))
    amount = models.FloatField(verbose_name=_('Amount'), blank=True, null=True)
    monthamount = models.FloatField(verbose_name=_('Month Amount'), blank=True, null=True)
    subtraction = models.FloatField(verbose_name=_('subtraction'))
    friendships = models.FloatField(verbose_name=_('Friendships and affections'))
    numberannual = models.FloatField(verbose_name=_('Annual number'))
    amountannual = models.FloatField(verbose_name=_('Annual Amount'))
    totalsubtraction = models.FloatField(verbose_name=_('Total Subtraction'))
    totalfriendships = models.FloatField(verbose_name=_('Total Friendships'))
    gifts = models.CharField(verbose_name=_('Title Gifts'), max_length=200)
    monthsequence = models.FloatField(verbose_name=_('Month Sequence'))
    paytype = models.IntegerField(verbose_name=_('Pay Type'), default=1, validators=[
                                  MaxValueValidator(12), MinValueValidator(1)])
    notes = models.TextField(verbose_name=_('Notes'), blank=True, null=True)

    class Meta:
        verbose_name = _('TableGift')
        verbose_name_plural = _('TableGifts')

    def __str__(self):
        return self.tablename.name

    def get_absolute_url(self):
        return reverse('TableGift_detail', kwargs={'pk': self.pk})


class TableGiftUser(models.Model):
    tablegift = models.ForeignKey(TableGift, verbose_name=_("Gift Tables"),
                                  on_delete=models.CASCADE, related_name='tabgiftuser')
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("TableGiftUser")
        verbose_name_plural = _("TableGiftUsers")

    def __str__(self):
        return str(self.id) + ' - ' + self.tablegift.tablename.name

    def get_absolute_url(self):
        return reverse("TableGift_detail", kwargs={"pk": self.pk})


class TableAmount(models.Model):
    tablegiftuser = models.OneToOneField(TableGiftUser, on_delete=models.CASCADE,
                                         verbose_name=_('Table Gift'), related_name=('amountgift'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    class Meta:
        verbose_name = _('TableAmount')
        verbose_name_plural = _('TableAmounts')

    def __str__(self):
        return str(self.id)+' - '+str(self.tablegiftuser.user.username)

    def get_absolute_url(self):
        return reverse('TableAmount_detail', kwargs={'pk': self.pk})


class TableInstallment(models.Model):
    tableamount = models.OneToOneField(TableGiftUser, verbose_name=_(
        'TableAmount'), on_delete=models.CASCADE, related_name='qst')
    payment = models.FloatField(verbose_name='Payment')

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("TableInstallment")
        verbose_name_plural = _("TableInstallments")

    def __str__(self):
        return str(self.id)+' - '+str(self.tableamount.tablegiftuser.user.username)

    def get_absolute_url(self):
        return reverse("TableInstallment_detail", kwargs={"pk": self.pk})
