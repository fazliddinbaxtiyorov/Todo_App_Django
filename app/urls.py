from django.urls import path
from .views import Home, adding_todo, update_todo, delete_todo, show
urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('new/', adding_todo, name='add_task'),
    path('update/<int:task_id>/', update_todo, name='update_task'),
    path('delete/<int:task_id>/', delete_todo, name='delete_task'),
    path('show/<int:task_id>/', show, name='task'),
]
