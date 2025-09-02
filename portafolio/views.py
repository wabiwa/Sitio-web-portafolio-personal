from django.shortcuts import render
from datetime import datetime, time

#más y menos ><

def Inicio(request):
    hora_actual = datetime.now().time()
    
    mañana = time(5,0,0)
    tarde = time(12,0,0)
    noche = time(20,0,0)

    if mañana <= hora_actual < tarde:
        bienvenida = "Buenos días"
        mensaje = "Al que madruga dios lo ayuda!"
    elif tarde <= hora_actual < noche:
        bienvenida = "Buenas tardes"
        mensaje = "¿Ya almorzaste?"
    else:
        bienvenida = "Buenas noches"
        mensaje = "¿No tienes sueño?"

    data = {"nombre":"Inicio", "bienvenida":bienvenida, "mensaje":mensaje}

    return render(request, 'inicio.html', data)

def Projects(request):
    projects = [{"title":"Proyecto A", "description":"Desarrollo web con Django",
    "in_progress":True, "image":"img1.jpg"},
    {"title":"Proyecto B", "description":"Aplicación móvil con Flutter",
    "in_progress":False, "image":"img2.png"},
    {"title":"Proyecto C","description":"Análisis de datos con Python",
    "in_progress":True, "image":"img3.jpg"},
    ]

    proyectos_en_progreso = [p for p in projects if p["in_progress"]]

    data = {"nombre":"Projects", "projects":proyectos_en_progreso}

    return render(request, 'projects.html', data)

def Contact(request):
    data = {"nombre":"Contact"}
    return render(request, 'contact.html',data)