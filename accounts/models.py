from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError(_('Users must have an username'))

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        user = self.create_user(username, password=password, **extra_fields)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name=_('Username'), max_length=120, unique=True)
    phone = models.CharField(verbose_name=_('Phone Number'), max_length=50, unique=False, blank=True, null=True)
    email = models.EmailField(verbose_name=_('Email'), unique=False, blank=True, null=True)
    regdate = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated'))
    is_active = models.BooleanField(default=True, verbose_name=_('is_active'))
    is_staff = models.BooleanField(default=False, verbose_name=_('is_staff'))
    is_superuser = models.BooleanField(default=False, verbose_name=_('is_superuser'))
    fcmtoken = models.CharField(max_length=500, verbose_name=_('FCM Token'), default=None, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
