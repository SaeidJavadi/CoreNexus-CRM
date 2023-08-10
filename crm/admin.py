from django.contrib import admin
from crm.models import Common60, Common61, Common70, CommonDead, JudiciaryDead, DoingDead, PublicAssistance, Lottery,\
    Notification, WinnerLottery60, GiftTable24, Installment, AmountGiftPay, TableGift1, TableGift2, TableGift3


@admin.register(Common60)
class Common60Admin(admin.ModelAdmin):
    class Meta:
        model = Common60
        fields = '__all__'


@admin.register(Common61)
class Common61Admin(admin.ModelAdmin):
    class Meta:
        model = Common61
        fields = '__all__'


@admin.register(Common70)
class Common70Admin(admin.ModelAdmin):
    class Meta:
        model = Common70
        fields = '__all__'


@admin.register(CommonDead)
class CommonDeadAdmin(admin.ModelAdmin):
    class Meta:
        model = CommonDead
        fields = '__all__'


@admin.register(JudiciaryDead)
class JudiciaryDeadAdmin(admin.ModelAdmin):
    class Meta:
        model = JudiciaryDead
        fields = '__all__'


@admin.register(DoingDead)
class DoingDeadAdmin(admin.ModelAdmin):
    class Meta:
        model = DoingDead
        fields = '__all__'


@admin.register(PublicAssistance)
class PublicAssistanceAdmin(admin.ModelAdmin):
    class Meta:
        model = PublicAssistance
        fields = '__all__'


@admin.register(Lottery)
class LotteryAdmin(admin.ModelAdmin):
    class Meta:
        model = Lottery
        fields = '__all__'


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdate', 'seedate', 'subject', 'see')
    pass

    class Meta:
        model = Notification
        fields = '__all__'


@admin.register(WinnerLottery60)
class WinnerLottery60Admin(admin.ModelAdmin):
    # list_display = ("name",)
    pass


@admin.register(GiftTable24)
class GiftTable24Admin(admin.ModelAdmin):
    class Meta:
        model = GiftTable24
        fields = '__all__'


@admin.register(Installment)
class InstallmentAdmin(admin.ModelAdmin):
    class Meta:
        model = Installment
        fields = '__all__'


@admin.register(AmountGiftPay)
class AmountGiftPayAdmin(admin.ModelAdmin):
    class Meta:
        model = AmountGiftPay
        fields = '__all__'


@admin.register(TableGift1)
class TableGift1Admin(admin.ModelAdmin):
    class Meta:
        model = TableGift1
        fields = '__all__'


@admin.register(TableGift2)
class TableGift2Admin(admin.ModelAdmin):
    class Meta:
        model = TableGift2
        fields = '__all__'


@admin.register(TableGift3)
class TableGift3Admin(admin.ModelAdmin):
    class Meta:
        model = TableGift3
        fields = '__all__'
