from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from project.authentication.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """User model that is used in this project. Email is the username field."""

    email = models.EmailField(_("Email Address"), unique=True)
    email_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
