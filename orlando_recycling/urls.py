"""
URL configuration for testproject project.

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
from os import environ
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Orlando Recycling Information API",
        default_version="v1",
        description="An API for Orlando recycling information\n\nRepository: https://github.com/anazworth/orlando-recycling",
        terms_of_service="https://github.com/anazworth",
    ),
    public=True,
    url=environ.get("DEV_API_URL") if environ.get("ENV") == "development" else None,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("items.urls")),
    path("api/v1/", include("items.urls")),
]

if environ.get("ENV") == "development":
    urlpatterns += [path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui")]