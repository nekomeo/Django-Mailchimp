import logging

from django.conf import settings
from django.core.mail import send_mail, BadHeaderError


logger = logging.getLogger(__name__)

def send_email(instance):
    try:
        subject = 'Test Contact Form'

        message = ('Sender Info:\n\tFull Name: {name}\n\t' 'Email: {email}\n\t' 'Message:\n\t{message}\n\t').format(
            name=instance.name,
            email=instance.email,
            message=instance.message,
        )

        send_mail(
            subject,
            message,
            settings.MAILCHIMP_USERNAME,
            fail_silently=True
        )
    except BadHeaderError:
        logger.error('Invalid header found')