__author__ = 'rayatnia'
import smtplib
from email.mime.text import MIMEText
from threading import Thread
from django.core.mail import send_mail
from django.conf import settings


def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper


def send_mails(subject, body, fr=settings.EMAIL_HOST_USER, to=[]):
    send_mail(
        subject,
        "",
        "robonit@nit.ac.ir",
        to,
        fail_silently=False,
        html_message=body)
