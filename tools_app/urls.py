from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from graphql_jwt.decorators import jwt_cookie

from api import views
from api.schema import schema
from api.views import graphql_docs
from tools_app import settings

urlpatterns = [
    settings.AUTH.urlpattern,
    path("", views.index),
    path("call_api", views.call_api, name="call_api"),
    path(
        "graphql/",
        jwt_cookie(csrf_exempt(GraphQLView.as_view(graphiql=False, schema=schema))),
    ),
    path("docs", graphql_docs, name="graphql_docs"),
    path("admin/", admin.site.urls),
]
