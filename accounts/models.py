from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, username, phone, password=None, **extra_fields):
        if not username:
            raise ValueError('Users must have an username')
        if not phone:
            raise ValueError('Users must have an phone')

        user = self.model(username=username, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        user = self.create_user(username, phone, password=password, **extra_fields)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name=_('Username'), max_length=255, unique=True)
    fullname = models.CharField(verbose_name=_('Full Name'), max_length=255)
    phone = models.BigIntegerField(verbose_name=_('Phone Number'), unique=True)
    email = models.EmailField(verbose_name=_('email'), max_length=255, unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name=_('is_active'))
    is_staff = models.BooleanField(default=False, verbose_name=_('is_staff'))
    is_superuser = models.BooleanField(default=False, verbose_name=_('is_superuser'))

    objects = UserManager()

    # We can use any field for username
    USERNAME_FIELD = 'username'  # or 'email' or 'phone'
    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
