from core import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('tools', views.ToolView, basename='Tools')
