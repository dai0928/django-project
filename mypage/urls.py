from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('program/', include('program.urls')),
    path('admin/', admin.site.urls),
]