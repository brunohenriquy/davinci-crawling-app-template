# -*- coding: utf-8 -*
# Copyright (c) 2019 BuildGroup Data Services Inc.

"""
{{ app_name | lower }} URL Configuration

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
from django.conf.urls import url, include

from rest_framework.schemas import get_schema_view

from caravaggio_rest_api.views import get_swagger_view

from {{ app_name | lower }}.api.urls import urlpatterns as {{ app_name | lower }}_urls

urlpatterns = [
    url(r'^api-schema/{{ app_name | lower }}/$',
        get_schema_view(title="{{ app_name | capfirst }} API",
                        patterns=[url(r'^{{ app_name | lower }}/',
                                      include({{ app_name | lower }}_urls))])),

    # {{ app_name | capfirst }} API version
    url(r'^{{ app_name | lower }}/', include({{ app_name | lower }}_urls)),
]
