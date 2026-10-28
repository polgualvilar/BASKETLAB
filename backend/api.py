from fastapi import FastAPI, HTTPException
from almacenamiento import cargar_jugadores, cargar_partidos
from consultas import buscar_jugador
from pydantic import BaseModel

app = FastAPI()

class JugadorEntrada(BaseModel):
    nombre: str
    dorsal: int
    posicion: str

@app.get("/")
def inicio():
    return{"mensaje": "Bienvenido a BasketLab"}

@app.get("/jugadores")
def obtener_jugadores():
    jugadores = cargar_jugadores()
    return jugadores

@app.get("/partidos")
def obtener_partidos():
    partidos = cargar_partidos()
    return partidos

@app.get("/jugadores/{dorsal}")
def obtener_jugador(dorsal: int):
    jugadores = cargar_jugadores()
    jugador = buscar_jugador(jugadores, dorsal)

    if jugador is None:
        raise HTTPException(
            status_code=404,
            detail="Jugador no encontrado"
        )
    return jugador

