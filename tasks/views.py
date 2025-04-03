from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

# Importa las clases necesarias de Django REST Framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer

# Vista para registrar un nuevo usuario
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Guardamos el nuevo usuario
            return redirect('login')  # Redirigimos al usuario al formulario de login
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})

# Vista para iniciar sesión
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirige a la lista de tareas
            return redirect('task_list')
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})

# Vista para cerrar sesión
def user_logout(request):
    logout(request)
    return redirect('login')

# Vista para listar las tareas del usuario autenticado
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)  # Filtra las tareas del usuario autenticado
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


# Vista para ver los detalles de una tarea específica
@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    return render(request, 'tasks/task_detail.html', {'task': task})

# Vista para crear una nueva tarea
@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

# Vista para editar una tarea existente
@login_required
def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

# Vista para eliminar una tarea
@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

# Vista para marcar una tarea como completada
@login_required
def task_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = True
    task.save()
    return redirect('task_list')


# Vista API para gestionar tareas utilizando Django REST Framework
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Modifica la consulta para que un usuario solo vea sus propias tareas.
        """
        return self.queryset.filter(user=self.request.user)

