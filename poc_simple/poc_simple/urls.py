from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from core.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', include('core.swagger')),
    path('docs/', include_docs_urls(title='API')),

    path('api/', include(router.urls)),
]
