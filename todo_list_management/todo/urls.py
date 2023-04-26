from django.urls import path
from .views import TaskList , TaskDetail , TaskCreate

urlpatterns=[
    path('tasks/',TaskList.as_view(),name='tasks'),
    path('tasks/task/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('create-task/',TaskCreate.as_view(),name='create'),
]