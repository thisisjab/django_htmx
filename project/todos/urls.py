from django.urls import include, path

from project.todos import htmx_views, views

app_name = "todo"

htmx_urlpatterns = [
    path("add/", htmx_views.add_todo, name="add"),
    path("delete/<int:pk>/", htmx_views.delete_todo, name="delete"),
]

urlpatterns = [
    path("list/", views.TodoListView.as_view(), name="list"),
    path("", include(htmx_urlpatterns)),
]
