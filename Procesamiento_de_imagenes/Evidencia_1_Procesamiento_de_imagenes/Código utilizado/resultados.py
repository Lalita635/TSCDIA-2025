# resultados.py
# Copyright (c) 2025 M. Laura Peralta
# Todos los derechos reservados.

import cv2
import matplotlib.pyplot as plt
from PIL import Image

def mostrar_resultados(img_cv2, contador_rotaciones, contador_recortes, contador_blur, contador_bordes, contador_binarias, contador_canny, imagenes_rotadas, imagenes_recortadas, imagenes_desenfocadas, imagenes_bordes, imagenes_canny, imagenes_binarias):
    img = img_cv2
    total = 1 + (contador_rotaciones - 1) + (contador_recortes - 1) + (contador_blur - 1) + (contador_bordes - 1) + (contador_binarias - 1) + (contador_canny - 1)

    if total == 1:
        print("No hay imágenes modificadas para mostrar.")
        return

    cols = 2
    rows = (total + 1) // cols
    plt.figure(figsize=(12, 5 * rows))
    idx = 1

    if img is not None:
        plt.subplot(rows, cols, idx)
        plt.imshow(img)
        plt.title("Imagen Original")
        plt.axis('off')
        idx += 1

    for img_rot, titulo in imagenes_rotadas:
        plt.subplot(rows, cols, idx)
        plt.imshow(img_rot)
        plt.title(titulo)
        plt.axis('off')
        idx += 1

    for img_rec, titulo in imagenes_recortadas:
        plt.subplot(rows, cols, idx)
        plt.imshow(img_rec)
        plt.title(titulo)
        plt.axis('off')
        idx += 1

    plt.tight_layout()
    plt.show()

    for img_blur, info in imagenes_desenfocadas:
        plt.subplot(rows, cols, idx)
        plt.imshow(img_blur)
        plt.title(f"Imagen desenfocada ({info})")
        plt.axis('off')
        idx += 1

    for img_borde, info in imagenes_bordes:
        plt.subplot(rows, cols, idx)
        plt.imshow(img_borde)
        plt.title(info)
        plt.axis('off')
        idx += 1

    for img_bin, info in imagenes_binarias:
        plt.subplot(rows, cols, idx)
        plt.imshow(img_bin, cmap='gray')
        plt.title(info)
        plt.axis('off')
        idx += 1

    for img_can, info in imagenes_canny:
        plt.subplot(rows, cols, idx)
        plt.imshow(img_can, cmap='gray')
        plt.title(info)
        plt.axis('off')
        idx += 1
  

import zipfile
import os
from google.colab import files

def exportar_zip(nombre_zip, img_cv2, imagenes_rotadas, imagenes_recortadas, imagenes_desenfocadas, imagenes_bordes, imagenes_binarias, imagenes_canny):
    with zipfile.ZipFile(nombre_zip, 'w') as zipf:
        
        if img_cv2 is not None:
            img_original = Image.fromarray(img_cv2)
            nombre_original = "imagen_original.jpg"
            img_original.save(nombre_original)
            zipf.write(nombre_original)

        for i, (img, _) in enumerate(imagenes_rotadas, start=1):
            nombre = f"rotada_{i}.jpg"
            img.save(nombre)
            zipf.write(nombre)

        for i, (img, _) in enumerate(imagenes_recortadas, start=1):
            nombre = f"recortada_{i}.jpg"
            img.save(nombre)
            zipf.write(nombre)

        for i, (img, _) in enumerate(imagenes_desenfocadas, start=1):
            nombre = f"blur_{i}.jpg"
            img.save(nombre)
            zipf.write(nombre)

        for i, (img, _) in enumerate(imagenes_bordes, start=1):
            nombre = f"bordes_{i}.jpg"
            img.save(nombre)
            zipf.write(nombre)

        for i, (img, _) in enumerate(imagenes_binarias, start=1):
            nombre = f"binaria_{i}.jpg"
            img.save(nombre)
            zipf.write(nombre)

        for i, (img, _) in enumerate(imagenes_canny, start=1):
            nombre = f"canny_{i}.jpg"
            img.save(nombre)
            zipf.write(nombre)

    files.download(nombre_zip)
    print(f"\nArchivo '{nombre_zip}' generado y descargado.")
