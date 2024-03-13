from django.db import models
from django.core.validators import RegexValidator


phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Формат телефона '+999999999'.")


class Type(models.TextChoices):
    COFFEE = 'Кофейня'
    RESTAURANT = 'Ресторан'
    SHOP = 'Магазин'


class QForm(models.Model):
    email = models.EmailField(max_length=50)
    company_name = models.CharField(max_length=100)
    prop_type = models.CharField(max_length=50, choices=Type.choices)
    is_franchise = models.BooleanField(default=False)
    address = models.CharField(max_length=256, blank=True)
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17, blank=True
        )
