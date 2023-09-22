from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from project.todos.models import Todo


class TodoListView(LoginRequiredMixin, generic.TemplateView):
    template_name = "todos/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_todos"] = Todo.objects.filter(user=self.request.user)
        return context
