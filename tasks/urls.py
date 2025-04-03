# tasks/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, register, user_login, user_logout, task_list, task_detail, task_create, task_edit, task_delete, task_complete

# Configura el enrutador para que maneje las rutas de la API
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    # Rutas de la API
    path('api/', include(router.urls)),  # Accede a la API a través de /api/
    
    # Rutas de autenticación
    path('register/', register, name='register'),  # Ruta de registro
    path('login/', user_login, name='login'),  # Ruta de login
    path('logout/', user_logout, name='logout'),  # Ruta de logout
    
    # Rutas tradicionales de tareas
    path('task-list/', task_list, name='task_list'),  # Lista de tareas
    path('task/<int:task_id>/', task_detail, name='task_detail'),  # Detalle de tarea
    path('task/create/', task_create, name='task_create'),  # Crear tarea
    path('task/<int:task_id>/edit/', task_edit, name='task_edit'),  # Editar tarea
    path('task/<int:task_id>/delete/', task_delete, name='task_delete'),  # Eliminar tarea
    path('task/<int:task_id>/complete/', task_complete, name='task_complete'),  # Completar tarea
]
