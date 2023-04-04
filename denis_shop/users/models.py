from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser


class Users(AbstractBaseUser, PermissionsMixin):
    pass
