import requests
import os
import bs4

#por algun motivo no se importan bien si intento hacer las funcones un modulo aparte
def url_bien(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url
    return url
def obtener_contenido(url):
    res = requests.get(url)
    res.raise_for_status()
    return res.text
def encontrar_imagenes(soup, base_url, dir_salida):
    img_tags = soup.find_all('img')
    for img_tag in img_tags:
        img_url = img_tag.get('src')
        if img_url.startswith(('http://', 'https://')):
            img_url = img_url
        else:
            img_url = base_url + img_url
        img_name = os.path.basename(img_url)
        img_path = os.path.join(dir_salida, img_name)
        with open(img_path, 'wb') as img_file:
            img_file.write(requests.get(img_url).content)
def elpedeefe(soup, base_url, dir_salida):
    pdf_tags = soup.find_all('a', href=lambda href: href and href.endswith('.pdf'))
    for pdf_tag in pdf_tags:
        pdf_url = pdf_tag.get('href')
        if not pdf_url.startswith(('http://', 'https://')):
            pdf_url = base_url + pdf_url
        pdf_name = os.path.basename(pdf_url)
        pdf_path = os.path.join(dir_salida, pdf_name)
        with open(pdf_path, 'wb') as pdf_file:
            pdf_file.write(requests.get(pdf_url).content)
def hipervinculo(soup, archivo_salida):
    links = []
    a_tags = soup.find_all('a', href=True)
    for a_tag in a_tags:
        link = a_tag['href']
        links.append(link)
    with open(archivo_salida, 'w') as f:
        f.write('\n'.join(links))
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
