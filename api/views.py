import random
import string

from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect
from graphene_django.views import GraphQLView
import requests
import graphdoc

__version__ = "0.2.0"

from graphql_jwt.refresh_token.shortcuts import create_refresh_token
from graphql_jwt.shortcuts import get_token


@settings.AUTH.login_required
def index(request, *, context):
    return redirect("call_api")


def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for i in range(length))


@settings.AUTH.login_required(scopes=["User.Read", "Directory.Read.All"])
def call_api(request, *, context):
    if context["access_token"]:
        api_result = requests.get(
            "https://graph.microsoft.com/v1.0/me/appRoleAssignments",
            headers={"Authorization": "Bearer " + context["access_token"]},
            timeout=30,
        )
        api_result2 = requests.get(
            "https://graph.microsoft.com/v1.0/me",
            headers={"Authorization": "Bearer " + context["access_token"]},
            timeout=30,
        )

        user_info = api_result2.json()
        user, created = User.objects.get_or_create(
            username=user_info["userPrincipalName"]
        )
        if created:
            app_role_id = api_result.json()["value"][0]["appRoleId"]
            if app_role_id == "0be6dabc-574d-4913-8652-befb6d290ed5":
                group, _ = Group.objects.get_or_create(name="manager")
            else:
                group, _ = Group.objects.get_or_create(name="user")
            user.groups.add(group)
            # Set a random password for the newly created user
            random_password = generate_random_password()
            user.set_password(random_password)
            user.save()

        jwt_token = get_token(user)
        refresh_token = create_refresh_token(user)
        authenticate(request, username=user.username, password=user.password)

        # Prepare the URL with tokens as query parameters
        redirect_url = f"http://localhost:3000/home?jwt_token={jwt_token}&refresh_token={refresh_token}"

        return redirect(redirect_url)


def graphql_docs(request):
    html = graphdoc.to_doc(GraphQLView().schema.graphql_schema)
    return HttpResponse(html, content_type="text/html")
