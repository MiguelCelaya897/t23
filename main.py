import requests
import os
import bs4
import modulos
def main():   
    url = input("Ingrese la URL a analizar: ")
    url = url_bien(url)
    contenidohtml = obtener_contenido(url)
    soup = bs4.BeautifulSoup(contenidohtml, 'html.parser')
    dir_salida = 'descarga'
    os.makedirs(dir_salida, exist_ok=True)
    encontrar_imagenes(soup, url, dir_salida)
    elpedeefe(soup, url, dir_salida)
    output_file = os.path.join(dir_salida, 'hyperlinks.txt')
    hipervinculo(soup, output_file)
    print("Proceso completado")
if __name__ == "__main__":
    main()
