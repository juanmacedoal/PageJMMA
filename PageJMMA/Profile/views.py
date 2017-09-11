from django.shortcuts import render
from django.views.generic import TemplateView

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