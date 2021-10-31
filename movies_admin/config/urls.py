from config.settings.base import STATIC_ROOT, STATIC_URL
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("movies.api.urls")),
] + static(STATIC_URL, document_root=STATIC_ROOT)
