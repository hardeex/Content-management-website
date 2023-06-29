from django.shortcuts import render, redirect, get_object_or_404
#from . import models
from .models import Tasks
from .forms import TaskForm
from django.views.generic import  CreateView, ListView, DeleteView
from django.urls import reverse_lazy, reverse
from django.views import View




# Create your views here.
class AddTaskView(CreateView):
    model = Tasks
    form_class = TaskForm
    template_name = 'tasks/add_tasks.html'
    success_url = reverse_lazy('tasks:tasks_list')

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)



    
class TaskListView(ListView):
    model = Tasks
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'
    ordering = ['due_date']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            # Filter tasks based on the logged-in user
            queryset = queryset.filter(user=self.request.user)
        else:
            # If user is not authenticated, return an empty queryset
            queryset = Tasks.objects.none()
        return queryset


class TaskCompleteView(View):
    def post(self, request):
        task_id = request.POST.get("completed")
        task = Tasks.objects.get(id=task_id)
        task.status = not task.status  # Toggle the status
        task.save()
        return redirect("tasks:tasks_list")


class DeleteCompletedTasksView(View):
    def post(self, request):
        Tasks.objects.filter(status=True).delete()
        return redirect("tasks:tasks_list")



class EditTaskView(View):
    def get(self, request, pk):
        task = get_object_or_404(Tasks, pk=pk)
        form = TaskForm(instance=task)
        return render(request, "tasks/edit_tasks.html", {"form": form, "task": task})

    def post(self, request, pk):
        task = get_object_or_404(Tasks, pk=pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks:tasks_list")
        return render(request, "tasks/edit_task.html", {"form": form, "task": task})



class DeleteTaskView(DeleteView):
    model = Tasks
    template_name = 'tasks/delete_task.html'
    success_url = reverse_lazy('tasks:tasks_list')





