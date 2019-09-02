<h1 align="center">Github Auth</h1>
<p align="left">
  A django application to login with github.
 </p>
<p>
  <a href="https://github.com/djangoapps/github_auth/blob/master/LICENSE" target="_blank">
    <img alt="MIT License" title="MIT License" src="https://img.shields.io/github/license/djangoapps/github_auth.svg?style=for-the-badge"/>
  </a>
  <a href="https://github.com/djangoapps/github_auth/releases" target="_blank">
    <img alt="releases" title="releases" src="https://img.shields.io/github/release/djangoapps/github_auth.svg?style=for-the-badge"/>
  </a>
  <img alt="last-commit" title="last-commit" src="https://img.shields.io/github/last-commit/djangoapps/github_auth.svg?style=for-the-badge"/>
  <a href="https://www.codacy.com/app/hakancelik96/github_auth?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=coogger/coogger&amp;utm_campaign=Badge_Grade" target="_blank">
 <img alt="Codacy Badge" title="Codacy Badge" src="https://img.shields.io/codacy/grade/8e73ecaa394440dfae5418bae3f71363?style=for-the-badge"/>
  </a>
  <a href="https://github.com/psf/black" target="_blank">
 <img alt="Code style" title="Code style" src="https://img.shields.io/badge/Code%20style-black-black?style=for-the-badge"/>
  </a>
   <a href="https://github.com/timothycrosley/isort" target="_blank">
 <img alt="Code style" title="Code style" src="https://img.shields.io/badge/code%20style-isort-lightgrey?style=for-the-badge"/>
  </a>
  <br>
</p>

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