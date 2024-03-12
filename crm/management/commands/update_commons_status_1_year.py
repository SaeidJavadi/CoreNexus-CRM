from django.core.management.base import BaseCommand, CommandError
from crm.models import Common60, Common61, Common70, CommonDead, JudiciaryDead
from datetime import datetime, timedelta
import logging


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Common60.objects.filter(created_on__lte=datetime.now()-timedelta(days=365)).update(pending_customer=False)
        oldstatus = True
        newstatus = False
        c60 = Common60.objects.filter(status=oldstatus)
        c60C = c60.count()
        c60.update(status=newstatus)

        c61 = Common61.objects.filter(status=oldstatus)
        c61C = c61.count()
        c61.update(status=newstatus)

        c70 = Common70.objects.filter(status=oldstatus)
        c70C = c70.count()
        c70.update(status=newstatus)

        cd = CommonDead.objects.filter(status=oldstatus)
        cdC = cd.count()
        cd.update(status=newstatus)

        jd = JudiciaryDead.objects.filter(status=oldstatus)
        jdC = jd.count()
        jd.update(status=newstatus)

        txt = f'\nUpdated status older than 365 days\nCommon60 count = {c60C}\nCommon61 count = {c61C}\nCommon70 count = {c70C}\nCommonDead count = {cdC}\nJudiciaryDead count = {jdC}\n{datetime.now()}\n'
        self.stdout.write(txt)
        logger = logging.getLogger("mylogger")
        logger.info(txt)
