from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscriptions, name='subscriptions'),
    path('subscription_success/<subscription_number>', views.subscription_success, name='subscription_success'),
]