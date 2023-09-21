from django.contrib import admin

from project.todos.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass
