from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """ Главная страница """

    template_name = 'main/home.html'
