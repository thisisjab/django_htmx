from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.timezone import datetime
from django.views.decorators.http import require_http_methods

from project.todos.models import Todo


@login_required
@require_http_methods(["POST"])
def add_todo(request):
    user = request.user
    todo_title = request.POST.get("todo_title")
    todo_due = request.POST.get("todo_due")
    user_last_todo = Todo.objects.filter(user=user).last()
    todo = Todo(
        user=user,
        title=todo_title,
        due=None if todo_due == "" else datetime.fromisoformat(todo_due),
        order=1 if user_last_todo is None else user_last_todo.order + 1,
    )

    todo.save()

    user_todos = Todo.objects.filter(user=user).order_by("order", "is_done")

    return render(
        request,
        "todos/partial/list.html",
        context={"user_todos": user_todos},
    )


@login_required
@require_http_methods(["DELETE"])
def delete_todo(request, pk):
    user = request.user
    todo_to_delete = Todo.objects.get(user=user, pk=pk)

    todo_to_delete.delete()

    user_todos = Todo.objects.filter(user=user).order_by("order", "is_done")

    return render(
        request,
        "todos/partial/list.html",
        context={"user_todos": user_todos},
    )


@login_required
@require_http_methods(["POST"])
def search_todo(request):
    user = request.user
    search_value = request.POST.get("search_value")
    found_todos = Todo.objects.filter(
        user=user,
        title__icontains=search_value,
    ).order_by("order", "is_done")

    return render(
        request,
        "todos/partial/list.html",
        context={"user_todos": found_todos},
    )


@login_required
@require_http_methods(["GET"])
def toggle_todo_is_done(request, pk):
    user = request.user
    todo = Todo.objects.get(user=user, pk=pk)

    todo.is_done = not todo.is_done

    todo.save()

    return render(
        request,
        "todos/partial/todo_item.html",
        context={"todo": todo},
    )


@login_required
@require_http_methods(["POST"])
def sort_todos(request):
    user = request.user
    user_todos = user_todos = Todo.objects.filter(user=user).order_by(
        "order",
        "is_done",
    )
    todo_orders = request.POST.getlist("todo_orders")
    for index, pk in enumerate(todo_orders, start=1):
        todo = Todo.objects.get(pk=pk)
        todo.order = index
        todo.save()

    user_todos = user_todos = Todo.objects.filter(user=user).order_by(
        "order",
        "is_done",
    )

    return render(
        request,
        "todos/partial/list.html",
        context={"user_todos": user_todos},
    )
