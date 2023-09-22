from django.contrib import admin
from django.urls import include, path

from project.authentication.urls import urlpatterns as authentication_urls
from project.todos.urls import urlpatterns as todo_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include((authentication_urls, "auth"), namespace="auth")),
    path("todo/", include((todo_urls, "todo"), namespace="todo")),
    path("__debug__/", include("debug_toolbar.urls")),
]
