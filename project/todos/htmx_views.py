from django.shortcuts import render
from django.utils.timezone import datetime

from project.todos.models import Todo


def add_todo(request):
    user = request.user
    todo_title = request.POST.get("todo_title")
    todo_due = request.POST.get("todo_due")
    todo = Todo(
        user=user,
        title=todo_title,
        due=None if todo_due == "" else datetime.fromisoformat(todo_due),
        order=Todo.objects.filter(user=user).last().order + 1 or 1,
    )

    todo.save()

    user_todos = Todo.objects.filter(user=user).order_by("order")

    return render(
        request,
        "todos/partial/list.html",
        context={"user_todos": user_todos},
    )


def delete_todo(request, pk):
    user = request.user
    todo_to_delete = Todo.objects.get(user=user, pk=pk)

    todo_to_delete.delete()

    user_todos = Todo.objects.filter(user=user).order_by("order")

    return render(
        request,
        "todos/partial/list.html",
        context={"user_todos": user_todos},
    )
