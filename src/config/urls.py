from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("api.rest.v1.urls")),
    path("", include("views.urls")),
]


if settings.SWAGGER_ENABLE:
    urlpatterns.extend(
        [
            path("api/schema.json", SpectacularAPIView.as_view(), name="schema"),
            path(
                "api/schema/swagger/",
                SpectacularSwaggerView.as_view(url_name="schema"),
                name="swagger",
            ),
        ]  # type: ignore
    )
