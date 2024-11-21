from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from accounts.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


countries = (
    ('Iraq', _('Iraq')),
    ('Iran', _('Iran')),
    ('Syria', _('Syria')),
    ('Sweden', _('Sweden')),
    ('Australia', _('Australia')),
    ('Denmark', _('Denmark')),
    ('Lebanon', _('Lebanon')),
    ('Saudi', _('Saudi')),
    ('Bahrain', _('Bahrain')),
    ('Kuwait', _('Kuwait')),
    ('Emirates', _('Emirates')),
    ('America', _('America')),
    ('India', _('India')),
    ('Pakistan', _('Pakistan')),
    ('Turkey', _('Turkey'))
)


class CommonsAmount(models.Model):
    title = models.CharField(verbose_name=_("Title"), max_length=150)
    name = models.CharField(verbose_name=_("Name"), max_length=150)
    amount = models.IntegerField(verbose_name=_("Amount"))
    createdt = models.DateTimeField(auto_now_add=True, verbose_name=_('Created Time'))
    updatedt = models.DateTimeField(auto_now=True, verbose_name=_('Updated Time'))

    class Meta:
        verbose_name = _("CommonsAmount")
        verbose_name_plural = _("CommonsAmounts")

    def __str__(self):
        return self.name + " - " + str(self.amount)

    def get_absolute_url(self):
        return reverse("CommonsAmount_detail", kwargs={"pk": self.pk})


class Common60(models.Model):   # Eshterak afrad 60 saal va kamtar
    usersubmit = models.ForeignKey(User, on_delete=models.CASCADE,
                                   verbose_name=_('Registrant'), related_name='user_c60')
    lottery = models.ForeignKey('LotteryC60', verbose_name=_(
        'lottery'), on_delete=models.SET_NULL, default=None, null=True, blank=True, related_name='lottery_c60')
    name = models.CharField(max_length=120, verbose_name=_('Quadruple common name'))
    age = models.IntegerField(verbose_name=_('Age'))
    idcode = models.PositiveBigIntegerField(verbose_name=_('Id Code'))
    sickness = models.CharField(verbose_name=_('sickness'), max_length=120, null=True, blank=True)
    contery = models.CharField(verbose_name=_('Contery'), max_length=120, choices=countries)
    city = models.CharField(verbose_name=_('State/City'), max_length=120)
    create = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    phone = models.CharField(verbose_name=_('Phone Number'), max_length=50)
    phoneagent = models.CharField(verbose_name=_('Phone Number Agent'), max_length=50)
    amount = models.ForeignKey(CommonsAmount, verbose_name=_('Amount'), on_delete=models.CASCADE)
    paystatus = models.BooleanField(verbose_name=_('PayStatus'), default=False)
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
    age = models.IntegerField(verbose_name=_('Age'))
    idcode = models.PositiveBigIntegerField(verbose_name=_('Id Code'))
    sickness = models.CharField(verbose_name=_('sickness'), max_length=120, null=True, blank=True)
    contery = models.CharField(verbose_name=_('Contery'), max_length=120, choices=countries)
    city = models.CharField(verbose_name=_('State/City'), max_length=120)
    create = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    phone = models.CharField(verbose_name=_('Phone Number'), max_length=50)
    phoneagent = models.CharField(verbose_name=_('Phone Number Agent'), max_length=50)
    amount = models.ForeignKey(CommonsAmount, verbose_name=_('Amount'), on_delete=models.CASCADE)
    paystatus = models.BooleanField(verbose_name=_('PayStatus'), default=False)
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
    age = models.IntegerField(verbose_name=_('Age'))
    idcode = models.PositiveBigIntegerField(verbose_name=_('Id Code'))
    sickness = models.CharField(verbose_name=_('sickness'), max_length=120, null=True, blank=True)
    contery = models.CharField(verbose_name=_('Contery'), max_length=120, choices=countries)
    city = models.CharField(verbose_name=_('State/City'), max_length=120)
    create = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    phone = models.CharField(verbose_name=_('Phone Number'), max_length=50)
    phoneagent = models.CharField(verbose_name=_('Phone Number Agent'), max_length=50)
    amount = models.ForeignKey(CommonsAmount, verbose_name=_('Amount'), on_delete=models.CASCADE)
    paystatus = models.BooleanField(verbose_name=_('Pay Status'), default=False)
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
    idcode = models.PositiveBigIntegerField(verbose_name=_('Id Code'))
    contery = models.CharField(verbose_name=_('Contery'), max_length=120, choices=countries)
    city = models.CharField(verbose_name=_('State/City'), max_length=120)
    create = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    phone = models.CharField(verbose_name=_('Phone Number'), max_length=50)
    phoneagent = models.CharField(verbose_name=_('Phone Number Agent'), max_length=50)
    amount = models.ForeignKey(CommonsAmount, verbose_name=_('Amount'), on_delete=models.CASCADE)
    paystatus = models.BooleanField(verbose_name=_('Pay Status'), default=False)
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
    idcode = models.PositiveBigIntegerField(verbose_name=_('Id Code'))
    contery = models.CharField(verbose_name=_('Contery'), max_length=120, choices=countries)
    city = models.CharField(verbose_name=_('State/City'), max_length=120)
    create = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    phone = models.CharField(verbose_name=_('Phone Number'), max_length=50)
    phoneagent = models.CharField(verbose_name=_('Phone Number Agent'), max_length=50)
    amount = models.ForeignKey(CommonsAmount, verbose_name=_('Amount'), on_delete=models.CASCADE)
    paystatus = models.BooleanField(verbose_name=_('Pay Status'), default=False)
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
    yearprayer = models.IntegerField(verbose_name=_('Years Passed prayer'))
    yearfasting = models.IntegerField(verbose_name=_('Years Passed fasting'))
    pilgrimage = models.CharField(max_length=200, verbose_name=_('Pilgrimage'))
    agent = models.CharField(max_length=200, verbose_name=_('Agent'))
    phone = models.CharField(verbose_name=_('Phone Number'), max_length=50)
    contery = models.CharField(verbose_name=_('Contery'), max_length=120, choices=countries)
    city = models.CharField(verbose_name=_('State/City'), max_length=120)
    deposit = models.FloatField(verbose_name=_('Deposit'))
    create = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    amount = models.ForeignKey(CommonsAmount, verbose_name=_('Amount'), on_delete=models.CASCADE)
    paystatus = models.BooleanField(verbose_name=_('Pay Status'), default=False)
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
    amount = models.ForeignKey(CommonsAmount, verbose_name=_('Amount'), on_delete=models.CASCADE)
    useramount = models.FloatField(verbose_name=_('User Amount'))
    paystatus = models.BooleanField(verbose_name=_('Pay Status'), default=False)
    status = models.BooleanField(verbose_name=_('Status'), default=False)

    class Meta:
        verbose_name = _('PublicAssistance')
        verbose_name_plural = _('PublicAssistances')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('PublicAssistance_detail', kwargs={'pk': self.pk})


class LotteryC60(models.Model):
    lottery_field = (
        ('quran', _('Quran memorization lottery')),
        ('ziarat', _('Visiting religious places'))
    )
    title = models.CharField(max_length=200, verbose_name=_('Lottery'), choices=lottery_field)
    name = models.CharField(max_length=30, verbose_name=_('Lottery Name'))

    class Meta:
        verbose_name = _('LotteryC60')
        verbose_name_plural = _('LotteryC60s')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('LotteryC60_detail', kwargs={'pk': self.pk})


class WinnerLottery60(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('Name'))
    common = models.ForeignKey('Common60', on_delete=models.CASCADE, related_name='winquran')
    lottery = models.ForeignKey('LotteryC60',  on_delete=models.CASCADE, related_name='winlottery')
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
    url = models.CharField(max_length=300, verbose_name=_('URL'), blank=True, null=True)
    force = models.BooleanField(default=False, verbose_name=_('Force Notification'))
    see = models.JSONField(verbose_name=_('See'), default={}, blank=True, null=True)

    class Meta:
        verbose_name = _('Notification')
        verbose_name_plural = _('Notifications')

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('Notification_detail', kwargs={'pk': self.pk})


class TableType(models.Model):
    name = models.CharField(verbose_name=_('Table Type'), max_length=150)
    footer = models.CharField(verbose_name=_('Footer'), max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = _("TableType")
        verbose_name_plural = _("TableTypes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tabletype_detail", kwargs={"pk": self.pk})


class TableGift(models.Model):
    tabletype = models.ForeignKey(TableType, verbose_name=_("Table Type"),
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
        return f'row.{self.id} - {self.tabletype.name}'

    def get_absolute_url(self):
        return reverse('TableGift_detail', kwargs={'pk': self.pk})


class TableGiftUser(models.Model):
    tablegift = models.ForeignKey(TableGift, verbose_name=_("Gift Tables"),
                                  on_delete=models.CASCADE, related_name='tabgiftusr')
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated'))
    active = models.BooleanField(verbose_name=_('Active'), default=True)
    countchances = models.IntegerField(verbose_name=_('Count of Chances'), default=1, validators=[MinValueValidator(1)])
    amount = models.IntegerField(verbose_name=_('Amount'))
    countpay = models.IntegerField(verbose_name=_('Count Pay'), validators=[MinValueValidator(1)])
    paystatus = models.BooleanField(verbose_name=_('Pay Status'), default=False)

    class Meta:
        verbose_name = _("TableGiftUser")
        verbose_name_plural = _("TableGiftUsers")

    def __str__(self):
        return 'Buy.'+str(self.id) + '-' + self.user.username + '_' + self.tablegift.tabletype.name

    def get_absolute_url(self):
        return reverse("TableGift_detail", kwargs={"pk": self.pk})


class TablePayment(models.Model):
    tabgiftusr = models.ForeignKey(TableGiftUser, on_delete=models.CASCADE,
                                   verbose_name=_('Table Gift User'), related_name=('pay'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    payment = models.FloatField(verbose_name=_('Payment'))
    status = models.BooleanField(verbose_name=_('Status'), default=False)

    class Meta:
        verbose_name = _('TablePayment')
        verbose_name_plural = _('TablePayments')

    def __str__(self):
        return 'Pay.' + str(self.tabgiftusr.id) + '-' + str(self.tabgiftusr.user.username)

    def get_absolute_url(self):
        return reverse('TablePayment_detail', kwargs={'pk': self.pk})


class WinTableLottery(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('Lottery Title'))
    tabgiftusr = models.ForeignKey(TableGiftUser, verbose_name=_("Table Gift User"),
                                   on_delete=models.CASCADE, related_name='tabwingift')
    windate = models.DateTimeField(auto_now_add=True, verbose_name=_('Win Date'))

    class Meta:
        verbose_name = _("WinTableLottery")
        verbose_name_plural = _("WinTableLotterys")

    def __str__(self):
        return f' WINNER -> {self.tabgiftusr.user.username}'

    def get_absolute_url(self):
        return reverse("WinTableLottery_detail", kwargs={"pk": self.pk})


class SocialMedia(models.Model):
    post_type = (
        ('post', _('Post')),
        ('story', _('Story'))
    )
    mediatype = models.CharField(verbose_name=_('Media Type'), max_length=5, choices=post_type, default=0)
    file = models.FileField(verbose_name=_('File'))
    caption = models.TextField(verbose_name=_('Caption'), blank=True, null=True)
    createdate = models.DateTimeField(auto_now_add=True, verbose_name=_('Create Date'))
    updatedate = models.DateTimeField(auto_now=True, verbose_name=_('Updated Time'))
    updatedt = models.DateTimeField(auto_now=True, verbose_name=_('Updated Time'))
    adv = models.BooleanField(verbose_name=_('Advertising'), default=False)
    active = models.BooleanField(verbose_name=_('Active'), default=True)

    class Meta:
        verbose_name = _("Social Media")
        verbose_name_plural = _("Social Media")

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return reverse("Postmedia_detail", kwargs={"pk": self.pk})


class ViewPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='viewuser')
    socialmedia = models.ForeignKey('SocialMedia', on_delete=models.CASCADE, related_name='viewpost')
    createdate = models.DateTimeField(auto_now_add=True, verbose_name=_('Create Date'))

    class Meta:
        unique_together = ('user', 'socialmedia')
        verbose_name = _("Post View")
        verbose_name_plural = _("Post Views")

    def __str__(self):
        return 'view_'+str(self.user)

    def get_absolute_url(self):
        return reverse("ViewPost_detail", kwargs={"pk": self.pk})


class LikePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likeuser')
    socialmedia = models.ForeignKey('SocialMedia', on_delete=models.CASCADE, related_name='likepost')
    createdate = models.DateTimeField(auto_now_add=True, verbose_name=_('Create Date'))

    class Meta:
        unique_together = ('user', 'socialmedia')
        verbose_name = _("Post Like")
        verbose_name_plural = _("Post Likes")

    def __str__(self):
        return 'like_'+str(self.user)

    def get_absolute_url(self):
        return reverse("Like_detail", kwargs={"pk": self.pk})


class CommentPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commentuser')
    socialmedia = models.ForeignKey('SocialMedia', on_delete=models.CASCADE, related_name='commentpost')
    text = models.TextField(verbose_name=_('Comment'), blank=False)
    active = models.BooleanField(verbose_name=_('Active'), default=True)
    createdt = models.DateTimeField(auto_now_add=True, verbose_name=_('Created Time'))
    updatedt = models.DateTimeField(auto_now=True, verbose_name=_('Updated Time'))

    class Meta:
        verbose_name = _("Comment Post")
        verbose_name_plural = _("Comment Posts")

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("CommentPost_detail", kwargs={"pk": self.pk})


class NewsText(models.Model):
    text = models.TextField(verbose_name=_('News Text'))
    createdt = models.DateTimeField(auto_now_add=True, verbose_name=_('Created Time'))
    updatedt = models.DateTimeField(auto_now=True, verbose_name=_('Updated Time'))
    active = models.BooleanField(verbose_name=_('Active'), default=False)

    class Meta:
        verbose_name = _("News Text")
        verbose_name_plural = _("News Texts")

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("NewsText_detail", kwargs={"pk": self.pk})
