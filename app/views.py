from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import TodoApp
from .forms import TodoForm

# Create your views here.


class Home(ListView):
    model = TodoApp
    template_name = 'app/index.html'
    context_object_name = 'todo'
    paginate_by = 6


def adding_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm()
    return render(request, 'app/add.html', {'form': form})


def update_todo(request, task_id):
    task = get_object_or_404(TodoApp, id=task_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('index')
    else:
        form = TodoForm(instance=task)
    return render(request, 'app/update.html', {'form': form, 'task': task})


def delete_todo(request, task_id):
    task = get_object_or_404(TodoApp, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    return render(request, 'app/delete.html', {'task': task})


def show(request, task_id):
    task = get_object_or_404(TodoApp, id=task_id)
    if request.method == 'POST':
        return redirect('index')
    return render(request, 'app/show.html', {'task': task})
