from django.shortcuts import render

# Importamos la función 'render' del módulo 'shortcuts' de Django

def index(request):
    # Definimos la función de vista 'index' que toma un objeto 'request' como argumento
    
    peliculas =[
        {
            'titulo':'AVATAR 2',
            'imagen':'https://www.elheraldo.co/sites/default/files/styles/width_1180/public/articulo/2022/09/23/fotojet_42.jpg?itok=9mYBiQdv'
        },
        {
            'titulo':'mario Bros',
            'imagen':'https://fs-prod-cdn.nintendo-europe.com/media/images/10_share_images/portals_3/2x1_SuperMarioHub_image1600w.jpg'
        },
        {
            'titulo':'shazam2',
            'imagen':'https://i0.wp.com/fugitives.com/wp-content/uploads/2023/03/Shazam-3-Storyline-Possibilities-Explained-2023-Action-Film.jpg'
        }
    ]
    # Creamos una lista llamada 'peliculas' que contiene tres diccionarios, cada uno representa una película con título e imagen.

    context={
        'peliculas':peliculas
    }
    # Creamos un diccionario llamado 'context' que contiene la clave 'peliculas' y le asignamos la lista 'peliculas'.

    return render(request, 'index.html', context)
    # Utilizamos la función 'render' para renderizar la plantilla 'index.html', pasando el objeto 'request' y el diccionario 'context' como argumentos.
