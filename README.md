<h1 align="center">Github Auth</h1>
<p align="left">
  A django application to login with github.
 </p>

[![MIT License](https://img.shields.io/github/license/coogger/github_auth.svg)](https://github.com/coogger/github_auth/blob/master/LICENSE) [![releases](https://img.shields.io/github/release/coogger/github_auth.svg)](https://github.com/coogger/github_auth/releases) [![last-commit](https://img.shields.io/github/last-commit/coogger/github_auth.svg)](https://github.com/coogger/github_auth/commits/master) [![Codacy Badge](https://img.shields.io/codacy/grade/8e73ecaa394440dfae5418bae3f71363)](https://app.codacy.com/manual/hakancelik96/github_auth) [![style](https://img.shields.io/badge/style-black-black)](https://github.com/psf/black) [![style](https://img.shields.io/badge/style-isort-lightgrey)](https://github.com/timothycrosley/isort) [![style](https://img.shields.io/badge/style-unimport-green)](https://github.com/coogger/github_auth) [![](https://img.shields.io/github/contributors/coogger/github_auth)](https://github.com/coogger/github_auth/graphs/contributors) [![](https://pepy.tech/badge/github-auth)](https://pepy.tech/badge/github-auth)

### 🚀 Installation and Usage 🚀

#### Installation
- Github Aauth can be installed by running `pip install github_auth`.

- Add "github_auth" to your INSTALLED_APPS setting:

```python
INSTALLED_APPS = []
    # …
    "github_auth",
]
```

- Set login and logout redirect url

```python
LOGIN_REDIRECT_URL = "/" # after users login, they will redirect this url
LOGOUT_REDIRECT_URL = "/" # after users logout
```

- Set your Github app configuration

```python
GITHUB_AUTH = dict(
    redirect_uri="your_redirect_uri",
    scope="your scope",
    client_secret="your github client_secret",
    client_id="your github client_id",
)
```

#### Usage

- In your **myapp/urls.py**:

```python

urlpatterns = [
    ...
    path("accounts/github/", include('github_auth.urls')),
]
```

- In your **myapp/templates**:

```html
<a href="{% url 'redirect-github' %}">login wia github</a>
```

- Github Auth extend default user model using `OneToOneField` so you can use as below.

> after login to show profile image from github profile image

```html
<img src="request.user.github_auth.avatar_url" title="request.user">
<p>{{request.user.github_auth.get_extra_data_as_dict.bio}}</p>
```

```python
request.user.github_auth.get_extra_data_as_dict.bio # and other extra_data fields
request.user.github_auth.avatar_url
```

or

```python
from django.contrip.auth.models import User

admin_avatar_url = User.objects.get(username="admin").github_auth.avatar_url

```

and you can use `next` field to redirect any addresses for example;
The user will be redirected to the same address after login.

```html
<a href="{% url 'redirect-github' %}?next={{ request.META.PATH_INFO }}">login wia github</a>
```

## Author / Social

👤 **Hakan Çelik** 👤

- [![](https://img.shields.io/twitter/follow/hakancelik96?style=social)](https://twitter.com/hakancelik96)
- [![](https://img.shields.io/github/followers/hakancelik96?label=hakancelik96&style=social)](https://github.com/hakancelik96)


## Version Notes

### V0.0.7
- Next attr added when login or logout
- Get email bug fixed
- Migrations files added


### V0.0.5
- View ( update githubuser ) bug fixed

### V0.0.2
- login
- logout
- get extra data
