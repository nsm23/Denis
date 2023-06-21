import uuid

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from PIL import Image

from phone_field import PhoneField

from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(
        _("uuid"), default=uuid.uuid4, unique=True, editable=False, auto_created=True
    )
    username = models.CharField(
        _("username"), unique=True, max_length=64, blank=True, db_index=True
    )
    avatar = models.ImageField(
        _("profile_foto"), default="default.jpg", upload_to="profile_pic", blank=True
    )
    birthday = models.DateField(_("birthday"), null=True, blank=True)
    email = models.EmailField(_("email"), unique=True)
    phone = PhoneField(_("phone"), blank=True, max_length=12)
    is_active = models.BooleanField(_("active"), default=True)
    is_staff = models.BooleanField(_("staff"), default=False)
    is_superuser = models.BooleanField(_("admin"), default=False)
    date_joined = models.DateTimeField(_("date_created"), auto_now_add=True)
    is_verified = models.BooleanField(_("verified"), default=False)
    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        unique_together = ("username", "email", "phone")

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def save_img(self):
        super().save_img()
        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)

    def __str__(self):
        return f"{self.username}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(_("first name"), max_length=128)
    surname = models.CharField(_("lastname"), max_length=256)

    def __str__(self):
        return f"{self.name} {self.surname}"
