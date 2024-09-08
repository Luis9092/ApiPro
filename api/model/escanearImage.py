from PIL import Image, ImageEnhance, ImageFont, ImageDraw
import cv2
import easyocr
import numpy as np
from api.model.mejorarImagen import MejorarImage

class EscanearImage():
    def __init__(self) -> None:
        pass
 
    def construnctorEscanearImage(self, imagen_path, font_path):
        ff = MejorarImage()
        retorno = ff.mejorarCalidad(imagen_path)
        reader = easyocr.Reader(["es", "en"], gpu=False,) 

        img = cv2.imread(retorno)
        result = reader.readtext(img)

        # Convertir la imagen de OpenCV a PIL
        img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img_pil)
        # image = cv2.cvtColor(np.array(img_pil), cv2.COLOR_BGR2RGB)
        cadena = ""

        for bbox, text, prob in result:
            # Extraer coordenadas del bounding box
            (tl, tr, br, bl) = bbox
            tl = (int(tl[0]), int(tl[1]))
            

            # Obtener el tamaño del texto
            font_size = 30  # Cambia el tamaño según sea necesario
            font = ImageFont.truetype(font_path, font_size)

            # Calcular la posición para colocar el texto
            text_x = tl[0]
            text_y = tl[1] - 28
 
            # Colocar el texto encima del bounding box
            draw.text((text_x, text_y), text, font=font, fill=(255, 0, 42))
            cadena += "\n"+ text +  " "

        print(cadena.strip())

        # Convertir la imagen de vuelta a OpenCV
        image = cv2.cvtColor(np.array(img_pil), cv2.COLOR_BGR2RGB)

        for bbox, text, prob in result:
            # Extraer coordenadas del bounding box
            (tl, tr, br, bl) = bbox
            tl = (int(tl[0]), int(tl[1]))
            br = (int(br[0]), int(br[1]))

            cv2.rectangle(image, tl, br, (33, 47, 86), 1)  # Aumentar grosor

        cv2.imwrite("api/imageServer/resultadoMarcado.png", image)

        return 1

        