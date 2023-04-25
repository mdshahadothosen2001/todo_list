from django.urls import path
from .views import TaskList , TaskDetail

urlpatterns=[
    path('tasks/',TaskList.as_view(),name='tasks'),
    path('tasks/task/<int:pk>/',TaskDetail.as_view(),name='task'),
]