import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from validaciones import comprobar_nombre, comprobar_dorsal

class TestValidaciones(unittest.TestCase):

    def test_nombre_espacios(self):

        resultado = comprobar_nombre("  Pol  ")

        self.assertEqual(resultado, "Pol")

    def test_nombre_solo_espacios(self):

        with self.assertRaises(ValueError):
            comprobar_nombre("   ")

    def test_dorsal_valido(self):

        jugadores = []

        resultado = comprobar_dorsal(23, jugadores)

        self.assertEqual(resultado, 23)

    def test_dorsal_ocupado(self):

        jugadores = [{"nombre": "Pol", "dorsal": 15, "posicion": "Exterior"}]

        with self.assertRaises(ValueError):
            comprobar_dorsal(15, jugadores)
