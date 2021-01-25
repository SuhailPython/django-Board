from django.db import models
from phone_field import PhoneField
# Create your models here.

class Info(models.Model):
    place = models.CharField(max_length=50000)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(max_length=254)


    class Meta:
        verbose_name = ("Info")
        verbose_name_plural = ("Infos")

    def __str__(self):
        return self.email


