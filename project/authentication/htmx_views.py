from django.http.response import HttpResponse

from project.authentication.models import User


def check_email(request):
    html_div = '<div class="alert alert-{}" role="alert">{}</div>'
    email = request.POST.get("email")
    if User.objects.filter(email=email).exists():
        return HttpResponse(html_div.format("danger", "Email already exists."))
    return HttpResponse(html_div.format("success", "You can use this email."))
