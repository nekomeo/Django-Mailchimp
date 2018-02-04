from django.db import models


class ContactForm(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    email = models.CharField(max_length=254)

    def __str__(self):
        return self.email
