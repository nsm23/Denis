from django.urls import path
from hubs.views import HubView


app_name = 'hub'

urlpatterns = [
    path('<str:slug_category>', HubView.as_view(), name='hub'),
]

