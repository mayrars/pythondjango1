import datetime
from django.http import HttpResponse
from django.template import Context, Template
def bienvenida(request):
    return HttpResponse("Bienvenido a mi pagina web en Django")
def bienvenida2(request):
    return HttpResponse("<p style='color: red'>Bienvenido a mi pagina web en Django</p>")

def contenidoHTML(request, nombre, edad):
    contenido = """
    <html>
    <body>
    <p>Nombre:%s / Edad:%s
    </p>
    </body>
    </html>
    """ % (nombre, edad)
    return HttpResponse(contenido)

def miPrimeraPlantilla(request):
    plantillaExterna = open("/var/www/html/django/MiProyecto/MiProyecto/plantillas/miPrimeraPlantilla.html")
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)

def plantillaParametros(request):
    nombre="Luisa"
    fechaActual = datetime.datetime.now()
    lenguajes = ["Python", "Java", "C#", "C++", "JavaScript"]
    plantillaExterna = open("/var/www/html/django/MiProyecto/MiProyecto/plantillas/plantillaParametros.html")
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context({"nombre":nombre, "fechaActual": fechaActual, "lenguajes":lenguajes})
    documento = template.render(contexto)
    return HttpResponse(documento)