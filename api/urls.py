# -*- coding: utf-8 -*
# Copyright (c) 2019 BuildGroup Data Services Inc.
"""
Company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2./topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include

from {{ app_name | lower }}.api.views import \
    {{ app_name | capfirst}}ResourceViewSet, \
    {{ app_name | capfirst }}ResourceSearchViewSet, \
    {{ app_name | capfirst }}ResourceGEOSearchViewSet

from rest_framework import routers

# API v1 Router. Provide an easy way of automatically determining the URL conf.

api_{{ app_name | upper }} = routers.DefaultRouter()

if settings.DSE_SUPPORT:
    api_{{ app_name | upper }}.register(r'{{ app_name | lower }}/search',
                            {{ app_name | capfirst }}ResourceSearchViewSet,
                            base_name="{{ app_name | lower }}-search")

    api_{{ app_name | upper }}.register(r'{{ app_name | lower }}/search/facets',
                            {{ app_name | capfirst }}ResourceSearchViewSet,
                            base_name="{{ app_name | lower }}-search-facets")

    api_{{ app_name | upper }}.register(r'{{ app_name }}/geosearch',
                            {{ app_name | capfirst }}ResourceGEOSearchViewSet,
                            base_name="{{ app_name | lower }}-geosearch")

api_{{ app_name | upper }}.register(r'{{ app_name }}',
                        {{ app_name | capfirst }}ResourceViewSet,
                        base_name="{{ app_name | lower }}")

urlpatterns = [
    # Company API version
    url(r'^', include(api_{{ app_name | upper }}.urls), name="{{ app_name | lower }}-api"),
]
