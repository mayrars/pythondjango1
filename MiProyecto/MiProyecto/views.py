from django.http import HttpResponse
def bienvenida(request):
    return HttpResponse("Bienvenido a mi pagina web en Django")
def bienvenida2(request):
    return HttpResponse("<p style='color: red'>Bienvenido a mi pagina web en Django</p>")

def categoriaEdad(request, edad):
    if edad >= 18:
        if edad>=60:
            categoria = "Eres mayor de edad y tienes mas de 60 años"
        else:
            categoria = "Eres mayor de edad"
    else:
        if edad < 10:
            categoria = "Eres menor de edad y tienes menos de 10 años"
        else:
            categoria = "Eres menor de edad"
    resultado = "<h1>Categoria de la edad: %s</h1>" %categoria

    return HttpResponse(resultado)
    