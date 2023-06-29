from django.urls import path
from . import views 
from . views import AddTaskView, TaskListView


app_name = 'tasks'
urlpatterns = [
    path('task_lists', TaskListView.as_view(), name='tasks_list'),
    path('add_tasks', AddTaskView.as_view() , name='add_tasks'),

    path("complete-task/", views.TaskCompleteView.as_view(), name="complete_task"),

    path("delete-completed-tasks/", views.DeleteCompletedTasksView.as_view(), name="delete_completed_tasks"),
    path("edit-task/<int:pk>/", views.EditTaskView.as_view(), name="edit_task"),
    path("delete-task/<int:pk>/", views.DeleteTaskView.as_view(), name="delete_task"),
]
