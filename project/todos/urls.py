from django.urls import path

from project.todos import views

app_name = "todo"
urlpatterns = [
    path("list/", views.TodoListView.as_view(), name="list"),
]
