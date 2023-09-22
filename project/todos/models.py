from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class Todo(models.Model):
    class State(models.TextChoices):
        DONE = "D", "Done"
        FINISHED = "F", "Finished"
        IN_PROGRESS = "I", "In Progress"
        PENDING = (
            "P",
            "Pending",
        )
        OVERDUE = "O", "Overdue"

    title = models.CharField(
        max_length=255,
        verbose_name=_("Title"),
        blank=False,
        null=False,
    )
    state = models.CharField(
        _("State"),
        max_length=2,
        choices=State.choices,
        default=State.PENDING,
    )
    due = models.DateField(blank=True, null=True, verbose_name=_("Due"))
    modification_time = models.DateTimeField(
        verbose_name=_("Modification Time"),
        auto_now=True,
    )
    order = models.PositiveIntegerField()
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_("User"),
    )

    class Meta:
        ordering = ["user", "order"]

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        # Get all todos with the same user and order greater than the current todo
        todos_to_update = Todo.objects.filter(user=self.user, order__gt=self.order)

        # Decrease the order of each todo by 1
        for todo in todos_to_update:
            todo.order -= 1
            todo.save()

        super().delete(*args, **kwargs)
