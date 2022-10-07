from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom user class to extend the base Django User class
    """

    twitter_account = models.CharField(
        "twitter account", null=True, blank=True, max_length=255, default="",
        help_text="The exact name of your twitter account"
    )

