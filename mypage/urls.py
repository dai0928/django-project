from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from registration import views

Index = TemplateView.as_view(template_name="registration/index.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Index, name="index"),
    path('', include("django.contrib.auth.urls")),
    path("create/", views.CreateAccountView.as_view(), name="create"),
    path("<str:username>/delete/", views.UserDeleteView.as_view(), name="delete"),
    path('program/', include('program.urls')),
]