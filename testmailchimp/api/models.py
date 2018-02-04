from django.db import models

# Create your models here.
class ContactForm(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    fullname = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    province_state = models.CharField(max_length=254)
    country = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    description = models.TextField()

    def __str__(self):
        return self.fullname + ' - ' + self.description[:20]
