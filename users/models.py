from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
import datetime


class UserModelManager(BaseUserManager):
    def create_user(self, email, password, full_name="", age=1, sex="other", address=None):
        if not email:
            raise ValueError("Email is required")

        user = self.model(email=self.normalize_email(
            email), full_name=full_name, age=age, sex=sex, address=address)
        user._set_user_unique_id()
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, full_name="", age=1, sex="other", address=None):
        user = self.create_user(email, password, full_name, age, sex, address)
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser):
    SEX_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other")
    )
    email = models.EmailField(verbose_name="email",
                              max_length=250, unique=True)
    date_joined = models.DateTimeField(
        verbose_name="date joined", auto_now_add=True, unique=True)
    user_unique_id = models.SlugField(unique=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    full_name = models.CharField(max_length=120, blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES,
                           default="other", blank=True, null=True)
    bio = models.TextField(max_length=250, blank=True, null=True)
    image_prof = models.ImageField(upload_to="images/users/", blank=True, null=True)
    tmp_token = models.CharField(max_length=6, blank=True, null=True)
    tmp_token_time = models.DateTimeField(blank=True, null=True)

    # created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ["username"]

    objects = UserModelManager()

    # def set_username(self):
    # self.username = str(self.email).split("@")[0]

    def __str__(self):
        # return str(self.email)
        return str(self.email).split("@")[0]

    def _set_user_unique_id(self):
        current_time = datetime.datetime.now()
        user_id = slugify(
            str(hex(int(str(slugify(current_time)).replace("-", ""))))[2:])
        self.user_unique_id = user_id

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_absolute_url(self):
        # return reverse("users:user_profile_page", kwargs={"pk": self.id})
        return reverse("users:user_profile_page", kwargs={"user_id": self.user_unique_id})
