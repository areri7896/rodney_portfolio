from django.core.mail import send_mail
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'cv/index.html', {})


def contact(request):
    if request.method == 'POST':
        name = request.POST['cname']
        email = request.POST['email']
        message = request.POST['message']

        subject = 'A Message from: ' + name + ' and email: ' + email
        send_mail(
            subject,
            message,
            email,
            ['arerirodney@yahoo.com', 'plpgroup25@gmail.com', 'arerirodney@gmail.com']
        )
    return render(request, 'cv/contact.html', {})


def resume(request):
    return render(request, 'cv/resume.html', {})


def portfolio(request):
    return render(request, 'cv/portfolio.html', {})


def about(request):
    return render(request, 'cv/about.html', {})
