# Uncomment the required imports before adding the code

# from django.shortcuts import render
# from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404, render, redirect
# from django.contrib.auth import logout
# from django.contrib import messages
# from datetime import datetime
# Importaciones necesarias

from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
import logging
import json
from django.views.decorators.csrf import csrf_exempt

# Obtén una instancia de un logger
logger = logging.getLogger(__name__)

# Crear una vista `login_user` para manejar solicitudes de inicio de sesión
@csrf_exempt
def login_user(request):
    # Obtener el nombre de usuario y la contraseña del cuerpo de la solicitud
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    
    # Intentar autenticar al usuario con las credenciales proporcionadas
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    
    if user is not None:
        # Si el usuario es válido, inicia sesión con el usuario actual
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    
    return JsonResponse(data)

# Crear una vista `logout_user` para manejar solicitudes de cierre de sesión
def logout_user(request):
    logout(request)  # Esto cierra la sesión del usuario
    data = {"userName": ""}
    return JsonResponse(data)

