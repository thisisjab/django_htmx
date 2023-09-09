from django.contrib import admin
from django.urls import include, path

from project.authentication.urls import urlpatterns as authentication_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include(authentication_urls)),
    path("__debug__/", include("debug_toolbar.urls")),
]
