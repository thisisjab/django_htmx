from django.urls import include, path

from project.authentication import htmx_views, views

app_name = "auth"

htmx_urlpatterns = [
    path("check-email/", htmx_views.check_email, name="check-email"),
]

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("", include(htmx_urlpatterns)),
]
