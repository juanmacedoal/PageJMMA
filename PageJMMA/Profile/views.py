from django.views.generic import TemplateView
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template.loader import get_template
from pprint import pprint
from .forms import ContactForm
from django.template import RequestContext, Context

pprint(globals())
pprint(locals())

# Create your views here.
def emailHome(request):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = 'PageJMMA '  + from_email + '   ' + form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['juanmacedoal@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return render(request, "index.html", {'form': form})

def email(request):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = 'PageJMMA '  + from_email + '   ' + form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['juanmacedoal@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return render(request, "curriculum.html", {'form': form})

class ProjectsPageView(TemplateView):
    template_name = 'projects.html'

class TutorialsPageView(TemplateView):
    template_name = 'tutorials.html'

class ArticlesPageView(TemplateView):
    template_name = 'articles.html'

class LanguagesPageView(TemplateView):
    template_name = 'languages.html'

class VideosPageView(TemplateView):
    template_name = 'videos.html'

    



