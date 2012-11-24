from celery.task import task, periodic_task
import datetime

from django.core.mail import send_mail, mail_admins


@periodic_task
def sample_email(run_every=datetime.timedelta(minutes=5)):
	mail_admins("This is a test!", "Test body at %s" % datetime.datetime.now())
	