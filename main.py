from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Aquí guardaremos los mensajes temporalmente en la memoria
mensajes_guardados = []

class Mensaje(BaseModel):
    texto: str
    autor: str

# Ruta para mostrar el Frontend
# 1. RUTA PARA EL FRONTEND: Muestra la página web al entrar
@app.get("/", response_class=HTMLResponse)
def mostrar_interfaz(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

# Ruta API para RECIBIR un mensaje del Frontend
@app.post("/api/mensajes")
def guardar_mensaje(msg: Mensaje):
    mensajes_guardados.append(msg)
    return {"status": "Mensaje recibido correctamente"}

# Ruta API para ENVIAR los mensajes al Frontend
@app.get("/api/mensajes")
def obtener_mensajes():
    return mensajes_guardados