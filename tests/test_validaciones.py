import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from validaciones import comprobar_nombre, comprobar_dorsal, comprobar_posicion, comprobar_rival, comprobar_id_partido

class TestValidaciones(unittest.TestCase):

    def setUp(self):
        self.jugadores = [
            {"nombre": "Pol", "dorsal": 15, "posicion": "Exterior"},
            {"nombre": "Victor", "dorsal": 30, "posicion": "Exterior"}
        ]

        self.posiciones = ["Interior", "Exterior"]

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

        with self.assertRaises(ValueError):
            comprobar_dorsal(15, self.jugadores)

    def test_conservar_dorsal(self):

        resultado = comprobar_dorsal(15, self.jugadores, jugador_actual=self.jugadores[0])

        self.assertEqual(resultado, 15)

    def test_cambiar_dorsal_ocupado(self):

        with self.assertRaises(ValueError):
            comprobar_dorsal(30, self.jugadores, jugador_actual=self.jugadores[0])

        self.assertEqual(self.jugadores[0]["dorsal"], 15)

    def test_dorsales_invalidos(self):

        dorsales_invalidos = [-1, "hola", True, 3.5]
        jugadores = []

        for dorsal in dorsales_invalidos:
            with self.subTest(dorsal=dorsal):
                with self.assertRaises(ValueError):
                    comprobar_dorsal(dorsal, jugadores)

    def test_dorsales_validos(self):

        dorsales_validos = [0, 1, 99]
        jugadores = []

        for dorsal in dorsales_validos:
            with self.subTest(dorsal=dorsal):
                resultado = comprobar_dorsal(dorsal, jugadores)
                self.assertEqual(resultado, dorsal)

    def test_posiciones_validas(self):
        entradas = ["INTERIOR", "interior", "Interior", "EXTERIOR", "exterior", "Exterior"]
        esperados = ["Interior", "Interior", "Interior", "Exterior", "Exterior", "Exterior"]
        

        for entrada, esperado in zip(entradas, esperados):
            with self.subTest(posicion=entrada):
                resultado = comprobar_posicion(entrada, self.posiciones)
                self.assertEqual(resultado, esperado)

    def test_posiciones_invalidas(self):
        entradas = ["", "Delantero", "Portero", "Mediocampista", 15, None, True]

        for entrada in entradas:
            with self.subTest(posicion=entrada):
                with self.assertRaises(ValueError):
                    comprobar_posicion(entrada, self.posiciones)

    def test_dorsales_limite(self):

        with self.assertRaises(ValueError):
            comprobar_dorsal(-1, self.jugadores)

        self.assertEqual(comprobar_dorsal(0, self.jugadores), 0)

        self.assertEqual(comprobar_dorsal(1, self.jugadores), 1)

    def test_ids_partidos_invalidos(self):

        ids_invalidos = [-1, "1", True, 3.5, None]

        for id in ids_invalidos:
            with self.subTest(id=id):
                with self.assertRaises(ValueError):
                    comprobar_id_partido(id)