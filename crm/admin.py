from django.contrib import admin
from crm.models import Common60, Common61, Common70, CommonDead, JudiciaryDead, DoingDead, PublicAssistance, Lottery, Notification


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
    list_display = ('user', 'createdate', 'seedate', 'subject', 'see')

    class Meta:
        model = Notification
        fields = '__all__'
