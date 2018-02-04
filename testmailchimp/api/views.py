from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializers import (ContactSerializer)

from .models import ContactForm


class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactSerializer

    # client = MailChimp(settings.MAILCHIMP_USERNAME, settings.MAILCHIMP_API_KEY)
    #
    # client.lists.members.create(settings.MAILCHIMP_LIST_ID, {
    #     'email_address': instance.email,
    #     'status': 'subscribed'
    # })
    http_method_names = ['post']
    permission_classes = [AllowAny]
