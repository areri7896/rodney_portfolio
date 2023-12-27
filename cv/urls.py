from django.contrib import admin
from django.urls import path

from cv import views as cv_views
urlpatterns = [
    path('', cv_views.index, name='home'),
    path('resume/', cv_views.resume, name='resume'),
    path('portfolio', cv_views.portfolio, name='portfolio'),
    path('contact', cv_views.contact, name='contact'),
    path('about', cv_views.about, name='about'),

]
