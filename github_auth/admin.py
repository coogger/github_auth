from django.contrib.admin import ModelAdmin, site
from django.http import Http404

#models
from .models import (
    GithubAuthUser, 
)

class GithubAuthUserAdmin(ModelAdmin):
    list_display = ["user"]
    list_display_links = list_display
    search_fields = list_display
    fields = [
        "user",
        "code",
        "access_token",
        "extra_data",
    ]

site.register(GithubAuthUser, GithubAuthUserAdmin)
