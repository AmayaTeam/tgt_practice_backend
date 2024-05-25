"""
URL configuration for tools_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from api import views
from api.schema import schema
from tools_app import settings

urlpatterns = [
    settings.AUTH.urlpattern,
    path('', views.index),
    # path("call_downstream_api", views.call_downstream_api),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    path('get_login_url/', views.get_login_url, name='get_login_url'),
    # path('getAToken/', views.get_atoken, name='get_atoken'),
    path("admin/", admin.site.urls),
]
