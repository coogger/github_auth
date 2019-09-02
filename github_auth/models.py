# django
# python
import ast

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _

AUTH_USER_MODEL = getattr(settings, "AUTH_USER_MODEL", User)


class GithubAuthUser(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.CharField(
        max_length=500, help_text=_("github user code / to get access_token")
    )
    access_token = models.CharField(
        max_length=500, help_text=_("github user access_token to any api operations")
    )
    extra_data = models.TextField()

    def __str__(self):
        return str(self.user)

    @property
    def get_extra_data_as_dict(self):
        return ast.literal_eval(self.extra_data)

    @property
    def avatar_url(self):
        return self.get_extra_data_as_dict.get("avatar_url")

    @property
    def username(self):
        return self.user.username
