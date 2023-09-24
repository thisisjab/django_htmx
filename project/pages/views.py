from django.views import generic


class IndexPageView(generic.TemplateView):
    template_name = "pages/index.html"
