from django.urls import path

from project.authentication import views

app_name = "auth"
urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
]
