from celery.decorators import periodic_task
from celery.schedules import crontab


@periodic_task(run_every=(crontab()))
def check_schedules():
    print("Done")

