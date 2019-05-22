# django
from django.db import models
from django.contrib.auth.models import User

class GithubAuthUser(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE
    )
    code = models.CharField(
        max_length = 500,
        help_text = "github user code / to get access_token"
    )
    access_token = models.CharField(
        max_length = 500,
        help_text = "github user access_token to any api operations"
    )
    extra_data = models.TextField()

    def __str__(self):
        return self.user

    @property
    def username(self):
        return self.user.username