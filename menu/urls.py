from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="menu/home.html"), name="home"),
    path(
        "services/",
        TemplateView.as_view(template_name="menu/services.html"),
        name="services",
    ),
    path(
        "services/web/", TemplateView.as_view(template_name="menu/web.html"), name="web"
    ),
    path("about/", TemplateView.as_view(template_name="menu/about.html"), name="about"),
    path(
        "contacts/",
        TemplateView.as_view(template_name="menu/contacts.html"),
        name="contacts",
    ),
    path(
        "services/design/",
        TemplateView.as_view(template_name="menu/design.html"),
        name="design",
    ),
    path("blog/", TemplateView.as_view(template_name="menu/blog.html"), name="blog"),
    path(
        "blog/news/", TemplateView.as_view(template_name="menu/blog.html"), name="blog"
    ),
    path(
        "blog/articles/",
        TemplateView.as_view(template_name="menu/articles.html"),
        name="articles",
    ),
    path(
        "support/",
        TemplateView.as_view(template_name="menu/support.html"),
        name="support",
    ),
]
