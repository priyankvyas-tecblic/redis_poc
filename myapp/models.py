from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Student(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    course = models.CharField(_("Course "), max_length=50)
    college = models.CharField(_("COllege"), max_length=50)