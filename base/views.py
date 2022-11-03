from django.shortcuts import render
from .models import Project
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.


def index(request):
    return render(request, 'base/index.html')



def send_email(request):
    if request.method == 'POST':
        template = render_to_string('base/email_template.html',{
            'name':request.POST['name'],
            'email':request.POST['email'],
            'msg':request.POST['msg'],
        })
        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['youminemyou@gmail.com']
        )
        email.fail_silently = False
        email.send()
    return render(request,'base/email_sent.html')

