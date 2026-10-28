import sys
import unittest
import tempfile
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from almacenamiento import (
    cargar_jugadores,
    guardar_jugadores,
    cargar_partidos,
    guardar_partidos)

class TestAlmacenamiento(unittest.TestCase):

    def test_guardar_jugadores(self):

        with tempfile.TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "jugadores.json"
            jugadores = [
                {"nombre": "Pol", "dorsal": 15, "posicion": "Exterior"},
                {"nombre": "Victor", "dorsal": 30, "posicion": "Exterior"}
            ]

            guardar_jugadores(jugadores, ruta)

            with open(ruta, "r", encoding="utf-8") as archivo:
                datos_guardados = json.load(archivo)

            self.assertEqual(datos_guardados, jugadores)

            jugadores_cargados = cargar_jugadores(ruta)
            self.assertEqual(jugadores_cargados, jugadores)

    def test_guardar_partidos(self):

        with tempfile.TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "partidos.json"

            partidos = [
                {"id": 1, "rival": "UE VETERANS BARBERA", "fecha": "16/10/2026", "lugar": "Visitante", "puntos_favor": 34, "puntos_contra": 54},
                {"id": 2, "rival": "BASKETVALL", "fecha": "21/10/2026", "lugar": "Local", "puntos_favor": 30, "puntos_contra": 35}
            ]

            guardar_partidos(partidos, ruta)

            with open(ruta, "r", encoding="utf-8") as archivo:
                partidos_guardados = json.load(archivo)

            self.assertEqual(partidos_guardados, partidos)

            partidos_cargados = cargar_partidos(ruta)
            self.assertEqual(partidos_cargados, partidos)

    def test_cargar_partidos_archivo_inexistente(self):

        with tempfile.TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "partidos_inexistente.json"

            resultado = cargar_partidos(ruta)

            self.assertEqual(resultado, [])