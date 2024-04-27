# Create your views here.
from Music_Therapy_API import settings
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
            settings.EMAIL_HOST_USER,
            ["cysbc1999@gmail.com"],
            auth_user=settings.EMAIL_HOST_USER,
            auth_password="Lovelife099!",
            fail_silently=False,
        )
    )
