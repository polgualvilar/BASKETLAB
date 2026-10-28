from fastapi import FastAPI, HTTPException
from almacenamiento import (
    cargar_jugadores,
    guardar_jugadores,
    cargar_partidos,
    guardar_partidos)
from consultas import buscar_jugador
from pydantic import BaseModel
from jugadores import crear_jugador
from partidos import crear_partido, registrar_partido

app = FastAPI()

class JugadorEntrada(BaseModel):
    nombre: str
    dorsal: int
    posicion: str

class PartidoEntrada(BaseModel):
    id: int
    rival: str
    fecha: str
    lugar: str
    puntos_favor: int
    puntos_contra: int

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

@app.post("/jugadores", status_code=201)
def registrar_jugador(datos: JugadorEntrada):
    jugadores = cargar_jugadores()

    try:
        jugador = crear_jugador(
            jugadores,
            datos.nombre,
            datos.dorsal,
            datos.posicion
        )

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        ) from error

    guardar_jugadores(jugadores)

    return jugador


@app.post("/partidos", status_code=201)
def registrar_partido_api(datos: PartidoEntrada):

    partidos = cargar_partidos()

    try:
        partido = crear_partido(
            id=datos.id,
            rival=datos.rival,
            fecha=datos.fecha,
            lugar=datos.lugar,
            puntos_favor=datos.puntos_favor,
            puntos_contra=datos.puntos_contra
        )

        registrar_partido(partidos, partido)

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        ) from error

    guardar_partidos(partidos)

    return partido



