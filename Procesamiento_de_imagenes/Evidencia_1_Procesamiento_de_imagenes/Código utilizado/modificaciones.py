# modificaciones.py
# Copyright (c) 2025 M. Laura Peralta
# Todos los derechos reservados.


# Rotar
def rotar_imagen(img_cv2, imagenes_rotadas, contador_rotaciones):
    from PIL import Image

    angulo = float(input("Ingrese el ángulo de rotación (en grados): "))

    img_pil = Image.fromarray(img_cv2)

    img_rotada = img_pil.rotate(-angulo, expand=True)

    nombre_archivo = f"rotada_{contador_rotaciones}.jpg"
    img_rotada.save(nombre_archivo)
    titulo = f"Rotación #{contador_rotaciones} ({angulo}°)"
    imagenes_rotadas.append((img_rotada, titulo))
    print(f"{titulo} guardada como '{nombre_archivo}'.")


# Recortar
def recortar_imagen(img_cv2, imagenes_recortadas, contador_recortes):
    from PIL import Image
    
    img = Image.fromarray(img_cv2)

    recortar = True
    while recortar:
      print("\nOpciones de recorte:")
      print("1 - Ingresar coordenadas manualmente")
      print("2 - Recortar el centro de la imagen (cuadrado)")
      opcion = input("Seleccione una opción de recorte (1 o 2): ")

      if opcion == "1":
          left = int(input("Izquierda (left): "))
          top = int(input("Superior (top): "))
          ancho = int(input("¿Cuántos px desea hacia la derecha?: "))
          alto = int(input("¿Cuántos px desea hacia abajo?: "))
          right = left + ancho
          bottom = top + alto

          compara1 = right > left 
          compara2 = bottom > top
          compara = compara1 + compara2
          if compara:
              img_recortada = img.crop((left, top, right, bottom))
              tipo = "manual"
              recortar = False
          else:
              print("Coordenadas inválidas.")
              return

      elif opcion == "2":
          img_width, img_height = img.size
          size = int(input("Tamaño del recorte cuadrado (ej: 400): "))
          if 0 < size <= img_width and size <= img_height:
              left = (img_width - size) // 2
              top = (img_height - size) // 2
              right = left + size
              bottom = top + size
              img_recortada = img.crop((left, top, right, bottom))
              tipo = "centrado"
              recortar = False
          else:
                print("Tamaño no válido.")
                return
      else:
          print("Opción de recorte no válida.")
          return

    nombre_archivo = f"recortada_{contador_recortes}.jpg"
    titulo = f"Recorte #{contador_recortes} ({tipo})"
    img_recortada.save(nombre_archivo)
    imagenes_recortadas.append((img_recortada, titulo))
    print(f"{titulo} guardado como '{nombre_archivo}'.")
    
# Blur
def desenfoque_gaussiano(img_cv2, imagenes_desenfocadas, contador_blur):
    from PIL import Image, ImageFilter

    img_pil = Image.fromarray(img_cv2)

    # Radio de desenfoque
    radio = 5
    opcion = input("\n¿Desea utilizar el radio por defecto (5)? (Si o No): ")

    if opcion.lower() == "si":
        pass
    elif opcion.lower() == "no":
        radio = int(input("Ingrese el radio a utilizar: "))
    else:
        print("Opción no válida. Se usará el valor por defecto.")
    
    img_blur = img_pil.filter(ImageFilter.GaussianBlur(radius=radio))

    nombre = f"blur_{contador_blur}.jpg"
    img_blur.save(nombre)
    titulo = f"Desenfoque #{contador_blur} (radio={radio})"
    imagenes_desenfocadas.append((img_blur, titulo))
    print(f"{titulo} guardada como '{nombre}'.")

# Bordes
def detectar_bordes(img_cv2, imagenes_bordes, contador_bordes):
    from PIL import Image, ImageFilter

    img_pil = Image.fromarray(img_cv2)
    img_edges = img_pil.filter(ImageFilter.FIND_EDGES)

    nombre = f"bordes_{contador_bordes}.jpg"
    img_edges.save(nombre)

    titulo = f"Bordes #{contador_bordes} (Filtro FIND_EDGES)"
    imagenes_bordes.append((img_edges, titulo))
    print(f"{titulo} guardada como '{nombre}'.")


# Binarización
def binarizar_imagen(img_cv2, imagenes_binarias, contador_binarias):
    import cv2
    from PIL import Image
    import numpy as np

    img_gris = cv2.cvtColor(img_cv2, cv2.COLOR_RGB2GRAY)
    _, img_binaria = cv2.threshold(img_gris, 127, 255, cv2.THRESH_BINARY)

    nombre = f"binaria_{contador_binarias}.jpg"
    cv2.imwrite(nombre, img_binaria)

    img_pil = Image.fromarray(img_binaria)
    titulo = f"Binarización #{contador_binarias}"
    imagenes_binarias.append((img_pil, titulo))
    print(f"{titulo} guardada como '{nombre}'.")


# Canny
def bordes_canny(img_cv2, imagenes_canny, contador_canny):
    import cv2
    from PIL import Image
    import numpy as np

    bordes = cv2.Canny(img_cv2, 100, 200)
    nombre = f"canny_{contador_canny}.jpg"
    cv2.imwrite(nombre, bordes)

    img_pil = Image.fromarray(bordes)
    titulo = f"Bordes Canny #{contador_canny}"
    imagenes_canny.append((img_pil, titulo))
    print(f"{titulo} guardada como '{nombre}'.")


def saludo():
  print("\n ----*****----")
  print("\nGracias por utilizar el script! :)")
  print("\Hasta la próxima")
  print("\n ----*****----")
