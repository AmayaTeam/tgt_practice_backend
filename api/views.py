import os
import json

import identity.django

import msal
from django.conf import settings
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.shortcuts import redirect, render, HttpResponse
import requests

__version__ = "0.2.0"

from graphql_jwt.refresh_token.shortcuts import create_refresh_token

from graphql_jwt.shortcuts import get_token


@settings.AUTH.login_required(scopes=["User.Read"])
def index(request, *, context):
    if context["access_token"]:
        # Получение информации о пользователе
        api_result = requests.get(  # Use access token to call an api
                    "https://graph.microsoft.com/v1.0/me/appRoleAssignments",
                    headers={'Authorization': 'Bearer ' + context['access_token']},
                    timeout=30,
                )
        api_result2 = requests.get(  # Use access token to call an api
            "https://graph.microsoft.com/v1.0/me",
            headers={'Authorization': 'Bearer ' + context['access_token']},
            timeout=30,
        )
        print(api_result.json())
        print(api_result2.json())
        user, created = User.objects.get_or_create(username=api_result2.json()['userPrincipalName'])
        if created and api_result.json()["value"][0]["appRoleId"] == "0be6dabc-574d-4913-8652-befb6d290ed5":
            group, _ = Group.objects.get(name='manager')
            user.groups.add(group)
        elif created and api_result.json()["value"][0]["appRoleId"] != "0be6dabc-574d-4913-8652-befb6d290ed5":
            group, _ = Group.objects.get(name='user')
            user.groups.add(group)


        # Создание JWT токена для пользователя
        jwt_token = get_token(user)
        print(jwt_token)
        refresh_token = create_refresh_token(user)
        print(refresh_token)

        response = JsonResponse({
            "access_token": jwt_token,
            "refresh_token": str(refresh_token),
        })
        print(response)
        response.set_cookie('jwt_token', jwt_token, httponly=True)
        return redirect("http://localhost:3000/home")

    return JsonResponse(status=400)
#
#
# @settings.AUTH.login_required(scopes=["User.Read"])
# def call_downstream_api(request, *, context):
#     api_result = requests.get(  # Use access token to call an api
#         "https://graph.microsoft.com/v1.0/me/appRoleAssignments",
#         headers={'Authorization': 'Bearer ' + context['access_token']},
#         timeout=30,
#     )
#     # if api_result.json["appRoleId"] == "0be6dabc-574d-4913-8652-befb6d290ed5":
#     #     print("Этот пользователь Manager")
#     return HttpResponse(json.dumps(api_result.json()), content_type="application/json")
#

def get_login_url(request):
    msal_app = msal.ConfidentialClientApplication(
        os.getenv('CLIENT_ID'),
        authority=os.getenv('AUTHORITY'),
        client_credential=os.getenv('CLIENT_SECRET')
    )
    auth_code_flow = msal_app.initiate_auth_code_flow(
        scopes=["User.Read"],
        redirect_uri=f"{os.getenv('REDIRECT_URI')}",

    )
    request.session['auth_code_flow'] = auth_code_flow
    auth_url = auth_code_flow['auth_uri']
    return JsonResponse({"auth_url": auth_url})


def get_atoken(request):
    auth_code_flow = request.session.get('auth_code_flow', {})
    msal_app = msal.ConfidentialClientApplication(
        os.getenv('CLIENT_ID'),
        authority=os.getenv('AUTHORITY'),
        client_credential=os.getenv('CLIENT_SECRET')
    )

    result = msal_app.acquire_token_by_auth_code_flow(auth_code_flow, request.GET)

    if "access_token" in result:
        access_token = result['access_token']

        # Получение информации о пользователе
        user_info = msal_app.acquire_token_silent(scopes=["User.Read"], account=None)
        email = user_info.get('id_token_claims', {}).get('preferred_username')

        user, created = User.objects.get_or_create(username=email, defaults={'email': email})
        if created:
            group, _ = Group.objects.get_or_create(name='default_group')
            user.groups.add(group)

        # Создание JWT токена для пользователя
        jwt_token = get_token(user)
        refresh_token = create_refresh_token(user)

        response = JsonResponse({
            "access_token": jwt_token,
            "refresh_token": str(refresh_token),
        })
        response.set_cookie('jwt_token', jwt_token, httponly=True)
        return response

    return JsonResponse(result, status=400)