import sys
import unittest
import tempfile
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from almacenamiento import cargar_jugadores, guardar_jugadores

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
