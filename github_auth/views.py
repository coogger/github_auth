# django
from django.views import View
from django.http import HttpResponseRedirect
from django.conf import settings
from django.http import Http404
from django.contrib.auth import logout, login
from django.contrib.auth.models import User

# models
from core.github_auth.models import GithubAuthUser

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
        email=extra_data.get("email")
        user_obj = User.objects.filter(username=username)
        user = user_obj[0]
        created = False
        if user_obj.exists():
            user_obj.update(email=email)
        else:
            user, created = User.objects.get_or_create(username=username, email=email)
        if created:
            GithubAuthUser(
                user=user, 
                code=code, 
                access_token=access_token, 
                extra_data=extra_data
            ).save()
        login(request, user, backend="django.contrib.auth.backends.ModelBackend")
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

    @staticmethod
    def convert_json(text):
        payload_to_json = dict()
        for i in text.split("&"):
            key, value = i.split("=")
            payload_to_json[key] = value
        return payload_to_json


class Logout(View):
    error = "There was an unexpected error while exiting"
    success = "See you again {}"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            ms.success(request,self.success.format(request.user))
            logout(request)
        return HttpResponseRedirect("/")