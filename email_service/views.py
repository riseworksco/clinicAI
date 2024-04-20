# Create your views here.
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.http import HttpResponse
from django.shortcuts import render

# def send_email(subject, body, email):
# try:
#     email_msg = EmailMessage(subject, body, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER], reply_to=[email])
#     email_msg.send()
#     print("Message sent :)")
#     return "Message sent :)"
# except:
#     print("Message failed, try again later :(")
#     return "Message failed, try again later :("


def send_test(request):
    return HttpResponse(
        send_mail(
            "SOJO Support Test",
            "test-body",
            "support@sojoai.com",
            ["cysbc1999@gmail.com"],
            auth_user="support@sojoai.com",
            auth_password="Lovelife099!",
            fail_silently=False,
        )
    )
