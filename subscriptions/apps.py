from django.apps import AppConfig


class SubscriptionsConfig(AppConfig):
    name = 'subscription'

    def ready(self):
        import subscription.signals
