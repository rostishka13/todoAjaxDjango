from django.shortcuts import render
from django.views.generic import View
from .models import Task
from .forms import TaskForm

# Create your views here.

class TaskList(View):
    def get(self, request):
        form = TaskForm()
        tasks = Task.objects.all()

        context = {'form': form, 'tasks': tasks}
        return render(request, 'base/task_list.html', context)