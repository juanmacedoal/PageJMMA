from django.conf.urls import url
from Profile import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]