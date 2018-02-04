from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from . import models

from mailchimp3 import MailChimp


@receiver(post_save, sender=models.ContactForm)
def send_email(instance, created, **kwargs):
    if not created:
        return

    client = MailChimp(settings.MAILCHIMP_USERNAME, settings.MAILCHIMP_API_KEY)

    client.lists.members.create(settings.MAILCHIMP_LIST_ID, {
        'email_address': instance.email,
        'status': 'subscribed'
    })
