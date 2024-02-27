from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter


def versioned_path(url, module, versions, add_without_version=True):
    versioned_urls = [
        path(
            f"{url}{version}/",
            include((module, module.split(".")[0]), namespace=version),
        )
        for version in versions
    ]
    if add_without_version:
        versioned_urls += [path(url, include(module))]
    return versioned_urls


def get_router():
    if settings.DEBUG:
        return DefaultRouter()
    else:
        return SimpleRouter()
