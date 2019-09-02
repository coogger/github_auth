# django
import json

# python
import requests
from django.conf import settings
from django.urls import path
from django.views.generic.base import RedirectView

# views
from .views import Github, Logout

github_params = settings.GITHUB_AUTH
redirect_uri = github_params.get("redirect_uri")
scope = github_params.get("scope")
client_secret = github_params.get("client_secret")
client_id = github_params.get("client_id")
authorize_url = f"https://github.com/login/oauth/authorize?\
    redirect_uri={redirect_uri}&scope={scope}&\
    cli\ent_secret={client_secret}&client_id={client_id}".replace(
    " ", ""
)

urlpatterns = [
    path("login/", Github.as_view(), name="login-via-github"),
    path("logout/", Logout.as_view(), name="logout"),
    path(
        "",
        RedirectView.as_view(url=authorize_url, permanent=False),
        name="redirect-github",
    ),
]
