from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.subscription, name='subscriptions'),
    path('subscription_success/<subscription_number>', views.subscription_success, name='subscription_success'),
    path('cache_subscription_data/', views.cache_subscription_data, name='cache_subscription_data'),
    path('wh/', webhook, name='webhook'),

]