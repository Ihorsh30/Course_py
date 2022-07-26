from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    """ Custom user model implementation """

    birth_date = models.DateField(null=True)
    wallet = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = "auth_user"
        verbose_name = "user"
        verbose_name_plural = "users"
