from django.urls import path
from .views import TodoViewSet, delete_all, delete_completed
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('todos', TodoViewSet, 'todos')

urlpatterns = [
    path("del-all/", delete_all, name="del-all"),
    path("del-completed/", delete_completed, name="del-completed")
]


urlpatterns += router.urls


# urlpatterns = [
#     path("", TodoViewSet.as_view({'get': "list"}))
# ]
