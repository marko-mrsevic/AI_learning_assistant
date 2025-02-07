from django.contrib.auth.base_user import BaseUserManager
# from django.contrib.auth.models import AbstractUser
# from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(
        self,
        email,
        password,
        **extra_fields
        ):

        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email) # lowercase the domain
        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password) # hash raw password and set
        user.save()
        return user
    def create_superuser(
        self,
        email,
        password,
        **extra_fields
        ):

        required_fields = {"is_staff": True, "is_superuser": True, "is_active": True}
        for key, value in required_fields.items():
            extra_fields.setdefault(key, value)
            if extra_fields[key] is not value:
                raise ValueError(
                    _(f"Superuser must have {key}={value}.")
                )
        return self.create_user(
            email,
            password,
            **extra_fields
        )