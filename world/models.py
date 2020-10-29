from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

class User(AbstractUser):
    """
    Users within the authentication system are represented by this model.
    Username and password are required. Other fields are optional.
    """

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

class Person(models.Model):
    """
    People in the virtch world are represented by this model.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('people')

class Reality(models.Model):
    """
    Realities of the virtch world are represented by this model.
    """
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = _('reality')
        verbose_name_plural = _('realities')
