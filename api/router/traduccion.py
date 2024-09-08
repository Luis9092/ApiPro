from fastapi import APIRouter, responses, Response
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from api.model.escanearImage import EscanearImage
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)
from numba import jit


traducir = APIRouter()


@traducir.get("/")
def root():
    return {"Escaneando": "Bienvenido"}


@jit
@traducir.get("/IniciarScanImage/<name>")
def iniciarScan(name: str):
    scan = EscanearImage()
    imagepath = "api/imageServer/" + name
    font_path = "api/lib/arial.ttf"
    retorno = scan.construnctorEscanearImage(imagen_path=imagepath, font_path=font_path)
    if retorno == 1:
        return Response(status_code=HTTP_200_OK)

    return Response(status_code=HTTP_404_NOT_FOUND)
