from django.views.generic import TemplateView
from Profile.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import Context
from django.template.loader import get_template



# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

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

class CurriculumPageView(TemplateView):
    template_name = 'curriculum.html'


def post(self, request, **kwargs):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact'
            , '')
            contact_email = request.POST.get(
                'email'
            , '')
            form_content = request.POST.get('message', '')

            # Email the profile with the 
            # contact information
            template = get_template('templates/contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['juanmacedoal@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('curriculum')

    return render(request, 'PageJMMA/Profile/templates/index.html', {
        'form': form_class,
    })