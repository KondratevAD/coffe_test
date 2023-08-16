from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUsers(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = "admin", _("Administrator")
        USER = "user", _("User")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ()
    email = models.EmailField(_("email"), unique=True)
    role = models.CharField(
        _("role"), choices=Roles.choices, default=Roles.USER, max_length=30
    )

    @property
    def is_admin(self):
        if self.role == "admin" or self.is_superuser:
            return True

    @property
    def is_user(self):
        if self.role == "user":
            return True

    class Meta:
        ordering = ("username",)


class Payments(models.Model):
    product = models.CharField(
        'Кофе',
        max_length=200,
    )
    user = models.ForeignKey(
        CustomUsers,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    price = models.PositiveBigIntegerField(
        'Цена',
    )
    currency = models.CharField(
        'Валюта',
        max_length=200,
    )
    pay_date = models.DateTimeField(
        'Дата покупки',

    )

    class Meta:
        ordering = ('pay_date',)
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'
