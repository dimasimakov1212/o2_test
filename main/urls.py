from django.urls import path


from main.apps import MainConfig
from main.views import HomePageView

app_name = MainConfig.name


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    ]
