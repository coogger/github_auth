# django
import json

# python
import requests
from django.conf import settings
from django.shortcuts import redirect
from django.urls import path
from django.views.generic.base import RedirectView

# views
from .views import Github, Logout


def redirect_github(requests):
    github_params = settings.GITHUB_AUTH
    redirect_uri = (
        github_params.get("redirect_uri") + f"?next={requests.GET.get('next')}"
    )
    scope = github_params.get("scope")
    client_secret = github_params.get("client_secret")
    client_id = github_params.get("client_id")
    return redirect(
        f"https://github.com/login/oauth/authorize?redirect_uri={redirect_uri}&scope={scope}&client_secret={client_secret}&client_id={client_id}"
    )


urlpatterns = [
    path("login/", Github.as_view(), name="login-via-github"),
    path("logout/", Logout.as_view(), name="logout"),
    path("", redirect_github, name="redirect-github"),
]
