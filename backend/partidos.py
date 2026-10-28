from config import lugares
from almacenamiento import guardar_partidos
from validaciones import (
    comprobar_id_partido,
    comprobar_rival,
    comprobar_fecha,
    comprobar_lugar,
    comprobar_puntos)

def crear_partido(id, rival, fecha, lugar, puntos_favor, puntos_contra):
   
    id = comprobar_id_partido(id)
    rival = comprobar_rival(rival)
    fecha = comprobar_fecha(fecha)
    lugar = comprobar_lugar(lugar, lugares)
    puntos_favor = comprobar_puntos(puntos_favor)
    puntos_contra = comprobar_puntos(puntos_contra)

    partido = {
        "id": id,
        "rival": rival,
        "fecha": fecha,
        "lugar": lugar,
        "puntos_favor": puntos_favor,
        "puntos_contra": puntos_contra
    }

    return partido

def registrar_partido(partidos, partido):

    for existente in partidos:
        if existente["id"] == partido["id"]:
            raise ValueError("Ya existe un partido con este ID.")
    
    partidos.append(partido)
    return partido


# ==========================================
# 4. REGISTRO DE PARTIDOS
# ==========================================

def agregar_partido(partidos):
    print("\n=== REGISTRAR PARTIDO ===")

    try:
        id_partido = int(input("ID del partido: "))
        rival = input("Nombre del rival: ")
        fecha = input("Fecha (DD/MM/AAAA): ")
        lugar = input("Lugar (Local/Visitante): ")
        puntos_favor = int(input("Puntos a favor: "))
        puntos_contra = int(input("Puntos en contra: "))

        partido = crear_partido(
            id=id_partido,
            rival=rival,
            fecha=fecha,
            lugar=lugar,
            puntos_favor=puntos_favor,
            puntos_contra=puntos_contra
        )

        registrar_partido(partidos, partido)
        guardar_partidos(partidos)

        print("\nPartido registrado correctamente.")

    except ValueError as error:
        print(f"\nError: {error}")
