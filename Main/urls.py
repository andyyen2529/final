from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.PMS),
    url(r'^customerAnalysis', views.customerAnalysis)

]