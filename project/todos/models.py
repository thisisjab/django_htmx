from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class Todo(models.Model):
    title = models.CharField(
        max_length=255, verbose_name=_("Title"), blank=False, null=False
    )
    description = models.TextField(verbose_name=_("Description"), blank=True, null=True)
    due = models.DateTimeField(blank=True, null=True, verbose_name=_("Due"))
    modification_time = models.DateTimeField(
        verbose_name=_("Modification Time"), auto_now=True
    )
    order = models.PositiveIntegerField()
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, verbose_name=_("User")
    )

    class Meta:
        ordering = ["user", "order"]

    def __str__(self):
        return self.title
