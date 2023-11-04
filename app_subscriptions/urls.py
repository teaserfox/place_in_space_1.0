from django.urls import path

from app_subscriptions.apps import AppSubscriptionsConfig
from app_subscriptions.views import SubscriptionsListView

app_name = AppSubscriptionsConfig.name

urlpatterns = [
    path("", SubscriptionsListView.as_view(), name="list"),
]
