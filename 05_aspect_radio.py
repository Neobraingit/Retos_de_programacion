'''/*
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/
 *   mouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
 */'''
 
import requests
from io import BytesIO
from PIL import Image

def calcular_aspect_ratio(url):
    # Descargar la imagen desde la URL
    response = requests.get(url)
    img_data = response.content

    # Abrir la imagen con PIL
    image = Image.open(BytesIO(img_data))

    # Obtener las dimensiones de la imagen
    width, height = image.size

    # Calcular el aspect ratio
    aspect_ratio = width / height

    # Devolver el aspect ratio
    return aspect_ratio

# URL de ejemplo
url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"

# Calcular y mostrar el aspect ratio
aspect_ratio = calcular_aspect_ratio(url)
print("Aspect Ratio:", aspect_ratio)
