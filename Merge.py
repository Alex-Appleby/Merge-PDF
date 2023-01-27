from PyPDF2 import PdfFileMerger
import os


# Con este código, convertimos solo los archivos que le indiquemos al programa
pdfs = ["1.pdf", "2.pdf"]
nombre_archivo_salida = "salida.pdf"
fusionador = PdfFileMerger()

for pdf in pdfs:
    fusionador.append(open(pdf, 'rb'))

with open(nombre_archivo_salida, 'wb') as salida:
    fusionador.write(salida)


# Con este código unimos todos los archivos que se encuentren en el directorio en el que nos encontramos
"""
 pdfs = [archivo for archivo in os.listdir('./') if archivo.endswith(".pdf")]
 nombre_archivo_salida = "salida.pdf"
 fusionador = PdfFileMerger()

 for pdf in pdfs:
     fusionador.append(open(pdf, 'rb'))

 with open(nombre_archivo_salida, 'wb') as salida:
     fusionador.write(salida)
"""
