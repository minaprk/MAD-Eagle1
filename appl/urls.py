from django.urls import path
from .import views
app_name = 'appl'
urlpatterns = [
    path("", views.index, name="index"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("service/", views.service, name="service"),
    path("about/", views.about, name="about"),
    path("blog/", views.blog, name="blog"),
    path('<int:article_id>/', views.detail, name = 'detail'),
    path("contact/", views.contact, name="contact"),
]
