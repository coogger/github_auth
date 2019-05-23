# github_auth
A django application to login with github.

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
{% url 'redirect-github' %}
```