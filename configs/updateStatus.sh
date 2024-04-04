#!/bin/bash
source /home/saeid/pyENV/bin/activate
python /home/saeid/projown/crm_ar/manage.py update_commons_status_1_year > /home/saeid/projown/crm_ar/zTMP/logs/updatestatus.log 2>&1

# CronJob
# At 00:00 on day-of-month 1 in January
# 0 0 1 1 * configs/updateStatus.sh