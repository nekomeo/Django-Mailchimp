from rest_framework import viewsets

from .serializers import (ContactSerializer)

from .models import ContactForm


class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactSerializer