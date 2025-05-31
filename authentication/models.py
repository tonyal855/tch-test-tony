from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

class CustomAuth(AbstractUser):
    ROLE_CHOICES = (
        ('manajer', 'Manajer'),
        ('user', 'User'),
        ('public', 'Public'),
    )
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE, default=0)
    module_id = models.IntegerField(default=0)
