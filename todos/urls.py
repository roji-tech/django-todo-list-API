from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", include("mytodos.urls")),
    path("api/", include("todo_api.urls")),
    path("admin/", admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('reg/', include('core.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/docs/', include_docs_urls(title='TodoAPI')),
    path('api/schema/', get_schema_view(
        title="TodoAPI",
        description="API for the Todos",
        version="1.0.0"
    ), name='todoapi-schema'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)