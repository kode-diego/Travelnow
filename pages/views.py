from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings


def home(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            emailTo = [settings.EMAIL_HOST_USER]
            try:
                send_mail(email, message, subject, emailTo)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('.')
    return render(request, "home.html", {'form': form})
