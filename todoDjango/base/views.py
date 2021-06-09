from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class TaskList(View):
    def get(self, request):
        return render(request, 'base/task_list.html')