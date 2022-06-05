from django.urls import path
from .views import TodoViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('todos', TodoViewSet, 'todos')

urlpatterns = router.urls


# urlpatterns = [
#     path("", TodoViewSet.as_view({'get': "list"}))
# ]
