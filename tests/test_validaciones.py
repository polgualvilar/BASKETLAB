import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from validaciones import (
    comprobar_nombre,
    comprobar_dorsal,
    comprobar_posicion,
    comprobar_rival,
    comprobar_id_partido,
    comprobar_fecha,
    comprobar_lugar,
    comprobar_puntos)
from config import lugares
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

    def test_fechas_validas(self):
        
        fechas_validas = [
            "28/10/2026",
            "01/01/2026",
            "15/01/2026",
            "10/03/2026"
        ]

        for fecha in fechas_validas:
            with self.subTest(fecha=fecha):
                resultado = comprobar_fecha(fecha)
                self.assertEqual(resultado, fecha)

    def test_fechas_invalidas(self):

        fechas_invalidas = [
            "31/02/2026",
            "32/10/2026",
            "28/13/2026",
            "2026-10-28",
            "5/1/2026",
            "",
            28102026,
            None
        ]

        for fecha in fechas_invalidas:
            with self.subTest(fecha=fecha):
                with self.assertRaises(ValueError):
                    comprobar_fecha(fecha)

    def test_lugares_validos(self):

        casos = [
            ("Local", "Local"),
            ("local", "Local"),
            ("LOCAL", "Local"),
            (" visitante ", "Visitante"),
            ("VISITANTE", "Visitante")
        ]

        for entrada, esperado in casos:
            with self.subTest(lugar=entrada):
                resultado = comprobar_lugar(entrada, lugares)
                self.assertEqual(resultado, esperado)

    def test_lugares_invalidos(self):
        lugares_invalidos = ["", "   ", "Neutral", "Casa", 123, None, True]

        for lugar in lugares_invalidos:
            with self.subTest(lugar=lugar):
                with self.assertRaises(ValueError):
                    comprobar_lugar(lugar, lugares)

    def test_puntos_validos(self):
        puntos_validos = [0, 1, 99]

        for puntos in puntos_validos:
            with self.subTest(puntos=puntos):
                resultado = comprobar_puntos(puntos)
                self.assertEqual(resultado, puntos)

    def test_puntos_invalidos(self):

        puntos_invalidos = [-1, "hola", True, 3.5, None]
                
        for puntos in puntos_invalidos:
            with self.subTest(puntos=puntos):
                with self.assertRaises(ValueError):
                    comprobar_puntos(puntos)