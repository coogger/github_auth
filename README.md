# github_auth
A django application to login with github.

### Install
`pip install github_auth`

### Usage

**/settings.py**

```python

INSTALLED_APPS = [
    ...
    ...
    ...
    "github_auth",
]

LOGIN_REDIRECT_URL = "/" # after users login, they will redirect this url
LOGOUT_REDIRECT_URL = "/" # after users logout
GITHUB_AUTH = dict(
    redirect_uri="your_redirect_uri",
    scope="your scope",
    client_secret="your github client_secret",
    client_id="your github client_id",
)

```

**/urls.py**

```python

urlpatterns = [
    ...
    ...
    ...
    path("accounts/github/", include('github_auth.urls')),
]

```

**/templates**

```
<a href="{% url 'redirect-github' %}">
    login wia github
</a>
```

```python
request.user.github_auth.get_extra_data_as_dict.name # and other fields
request.user.github_auth.avatar_url
```