import os
import json

from django.conf import settings
from django.shortcuts import redirect, render, HttpResponse
import requests


__version__ = "0.2.0"


@settings.AUTH.login_required
def index(request, *, context):
    user = context['user']
    return HttpResponse(f"Hello, {user.get('name')}.")


@settings.AUTH.login_required(scopes=["User.Read"])
def call_downstream_api(request, *, context):
    api_result = requests.get(  # Use access token to call an api
        "https://graph.microsoft.com/v1.0/me/appRoleAssignments",
        headers={'Authorization': 'Bearer ' + context['access_token']},
        timeout=30,
    )
    # if api_result.json["appRoleId"] == "0be6dabc-574d-4913-8652-befb6d290ed5":
    #     print("Этот пользователь Manager")
    return HttpResponse(json.dumps(api_result.json()), content_type="application/json")