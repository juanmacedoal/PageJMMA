from django.conf.urls import url
from Profile import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^projects/$', views.ProjectsPageView.as_view()),
    url(r'^tutorials/$', views.TutorialsPageView.as_view()),
    url(r'^videos/$', views.VideosPageView.as_view()),
    url(r'^languages/$', views.LanguagesPageView.as_view()),
    url(r'^articles/$', views.ArticlesPageView.as_view()),
  
]