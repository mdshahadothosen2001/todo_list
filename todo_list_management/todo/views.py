from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Task


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    #django can load by defualt template
    #but template name should be match class name
    # like if class name is TaskList
    #template name must be task_list.html
    template_name = 'todo/task_list.html'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/task_detail.html'    
    

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    template_name = 'todo/task_form.html' 


        