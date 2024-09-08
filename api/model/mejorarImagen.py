from PIL import Image, ImageEnhance, ImageFont, ImageDraw

class MejorarImage():
    def __init__(self) -> None:
        pass
    
    def mejorarCalidad(self, imagen_path):
        imagen = Image.open(imagen_path)

        # Aumentar la nitidez
        enhancer = ImageEnhance.Sharpness(imagen)
        imagen_mejorada = enhancer.enhance(2)  # Factor de aumento de nitidez

        # Aumentar el contraste
        enhancer_contraste = ImageEnhance.Contrast(imagen_mejorada)
        imagen_final = enhancer_contraste.enhance(1.5)  # Factor de aumento de contraste

        # Guardar la imagen mejorada en alta calidad
        imagen_final.save("imagen_mejorada.png", quality=100)
        # # Guardar la imagen mejorada

        return "imagen_mejorada.png"