from django.db.models.signals import post_save, post_delete
from .models import Subscription


@receiver(post_save, sender=Subscription)
def update_on_save(sender, instance, created, **kwargs):
    """ subscription total """
    instance.Subscription.update_total()


@receiver(post_delete, sender=Subscription)
def update_on_save(sender, instance, **kwargs):
    """ subscription total """
    instance.Subscription.update_total()