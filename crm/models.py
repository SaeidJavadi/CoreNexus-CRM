from django.db import models
from accounts.models import User
from django.utils.translation import gettext_lazy as _


class Common60(models.Model):   # Eshterak afrad 60 saal va kamtar
    usersubmit = models.ForeignKey(User, on_delete=models.CASCADE,
                                   verbose_name=_('Registrant'), related_name='user_c60')
    name = models.CharField(max_length=120, verbose_name=_('Quadruple common name'))
    age = models.DateField(verbose_name=_('Age'))
    idcode = models.IntegerField(verbose_name=_('Id Code'))
    sickness = models.CharField(verbose_name=_('sickness'), max_length=120)
    contery = models.CharField(verbose_name=_('Contery/State'), max_length=120)
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
        return self.name

    def get_absolute_url(self):
        return reverse('_detail', kwargs={'pk': self.pk})


class Common61(models.Model):  # Eshterak afrad az 61 ta 69
    usersubmit = models.ForeignKey(User, on_delete=models.CASCADE,
                                   verbose_name=_('Registrant'), related_name='user_c61')
    name = models.CharField(max_length=120, verbose_name=_('Quadruple common name'))
    age = models.DateField(verbose_name=_('Age'))
    idcode = models.IntegerField(verbose_name=_('Id Code'))
    Sickness = models.CharField(verbose_name=_('sickness'), max_length=120)
    contery = models.CharField(verbose_name=_('Contery/State'), max_length=120)
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
    Sickness = models.CharField(verbose_name=_('sickness'), max_length=120)
    contery = models.CharField(verbose_name=_('Contery/State'), max_length=120)
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
    contery = models.CharField(verbose_name=_('Contery/State'), max_length=120)
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
    contery = models.CharField(verbose_name=_('Contery/State'), max_length=120)
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
    contery = models.CharField(verbose_name=_('Contery/State'), max_length=120)
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
