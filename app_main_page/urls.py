from django.urls import path
from app_main_page.apps import AppMainPageConfig
from app_main_page.views import AppMainPageView

app_name = AppMainPageConfig.name

urlpatterns = [
    path('', AppMainPageView.as_view(), name='main'),
]
