from rest_framework.routers import DefaultRouter

from task_manager.api.public.views import *


app_name = 'task_public'

urlpatterns = [
]

router = DefaultRouter()

router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns += router.urls
