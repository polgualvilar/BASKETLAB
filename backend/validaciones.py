from consultas import buscar_jugador
from datetime import datetime
from config import lugares


def solicitar_nombre():
    while True:
        nombre = input("Introduce nombre: ").strip()

        if nombre == "":
            print("Introduce un nombre válido.")
        else:
            return nombre

def solicitar_dorsal(jugadores, jugador_actual=None):
    while True:
        try:
            dorsal = int(input("Introduce dorsal: "))

            return comprobar_dorsal(dorsal, jugadores, jugador_actual)

        except ValueError as error:
            print(f"Error: {error}")

def solicitar_posicion(posiciones):
    while True:
        posicion = input("Introduce posición: ").strip().capitalize()

        if posicion not in posiciones:
            print("Error: posición no válida.")
        else:
            return posicion

def comprobar_nombre(nombre):
    if nombre.strip() == "":
        raise ValueError("El nombre no puede estar vacío.")
    
    return nombre.strip()

def comprobar_dorsal(dorsal, jugadores, jugador_actual=None):

    if not isinstance(dorsal, int) or isinstance(dorsal, bool):
        raise ValueError("El dorsal debe ser un número entero.")

    if dorsal < 0:
        raise ValueError("El dorsal no puede ser negativo.")

    jugador_existente = buscar_jugador(jugadores, dorsal)
    if jugador_existente is not None and jugador_existente is not jugador_actual:
        raise ValueError("Este dorsal pertenece a otro jugador.")
    
    return dorsal

def comprobar_posicion(posicion, posiciones):

    if not isinstance(posicion, str):
            raise ValueError("La posición debe ser una cadena de texto.")

    posicion = posicion.strip().capitalize()
    
    if posicion not in posiciones:
        raise ValueError("Posición no válida.")
    
    return posicion

def comprobar_id_partido(id_partido):

    if not isinstance(id_partido, int) or isinstance(id_partido, bool):
            raise ValueError("El id debe ser un número entero.")
    
    if id_partido < 0:
        raise ValueError("El id no puede ser negativo.")
        
    return id_partido

def comprobar_rival(rival):
    if not isinstance(rival, str):
        raise ValueError("El rival debe ser texto")
    
    if rival.strip() == "":
            raise ValueError("El rival no puede estar vacío.")
        
    return rival.strip()

def comprobar_fecha(fecha):
    if not isinstance(fecha, str):
        raise ValueError("La fecha debe ser texto")
    
    try:
        fecha_convertida = datetime.strptime(fecha, "%d/%m/%Y")
    except ValueError:
        raise ValueError("La fecha debe ser válida y tener formato exacto DD/MM/AAAA.")

    if fecha_convertida.strftime("%d/%m/%Y") != fecha:
        raise ValueError("La fecha debe tener el formato exacto DD/MM/AAAA.")

    return fecha

def comprobar_lugar(lugar,lugares):

    if not isinstance(lugar, str):
        raise ValueError("El lugar debe ser una cadena de texto.")
    
    lugar = lugar.strip().capitalize()
        
    if lugar not in lugares:
            raise ValueError("Lugar no válido.")

    return lugar

def comprobar_puntos(puntos):

    if not isinstance(puntos, int) or isinstance(puntos, bool):
            raise ValueError("Los puntos deben ser un número entero.")
    
    if puntos < 0:
        raise ValueError("Los puntos no pueden ser negativo.")

    return puntos