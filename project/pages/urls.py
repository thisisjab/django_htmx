from django.urls import path

from project.pages import views

app_name = "pages"
urlpatterns = [path("", views.IndexPageView.as_view(), name="index")]
