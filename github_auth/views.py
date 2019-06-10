# django
from django.views import View
from django.http import HttpResponseRedirect
from django.conf import settings
from django.http import Http404
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib import messages

# models
from .models import GithubAuthUser

# python
import requests, json
# conf
github_params = settings.GITHUB_AUTH

class Github(View):
    access_token_api_url = "https://github.com/login/oauth/access_token"
    user_api_url = "https://api.github.com/user"

    def get(self, request, *args, **kwargs):
        code = request.GET.get("code", None)
        if code is None:
            raise Http404
        github_params.__setitem__("code", code)
        r = requests.post(self.access_token_api_url, params=github_params)
        access_token = self.convert_json(r.text).get("access_token", None)
        if access_token is None:
            raise Http404
        extra_data = requests.get(
            self.user_api_url,
            headers={"Authorization": f"token {access_token}"}
        )
        extra_data = json.loads(extra_data.text)
        username = extra_data.get("login")
        email = extra_data.get("email")
        user, created = User.objects.get_or_create(username=username)
        if created:
            GithubAuthUser(
                user=user,
                code=code,
                access_token=access_token,
                extra_data=extra_data
            ).save()
        else:
            github_user = GithubAuthUser.objects.get(user=user)
            github_user.code = code
            github_user.access_token = access_token
            github_user.extra_data = extra_data
            github_user.save()
        login(request, user, backend="django.contrib.auth.backends.ModelBackend")
        user.email = email
        try:
            user.save()
        except IntegrityError:
            pass
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

    @staticmethod
    def convert_json(text):
        payload_to_json = dict()
        for i in text.split("&"):
            key, value = i.split("=")
            payload_to_json[key] = value
        return payload_to_json


class Logout(View):
    success = "See you again {}"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(request, self.success.format(request.user))
            logout(request)
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)
