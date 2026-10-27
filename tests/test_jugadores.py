
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from jugadores import crear_jugador, actualizar_jugador


class TestJugadores(unittest.TestCase):

    def test_crear_jugador(self):
        jugadores = []

        nuevo = crear_jugador(
            jugadores,
            "Marc",
            10,
            "Interior"
        )

        self.assertEqual(nuevo["nombre"], "Marc")
        self.assertEqual(nuevo["dorsal"], 10)
        self.assertEqual(nuevo["posicion"], "Interior")
        self.assertEqual(len(jugadores), 1)

    def test_dorsal_duplicado(self):
        jugadores = []

        crear_jugador(jugadores, "Pol", 15, "Exterior")

        with self.assertRaises(ValueError):
            crear_jugador(jugadores, "Marc", 15, "Interior")

        self.assertEqual(len(jugadores), 1)

    def test_nombre_vacio(self):
        jugadores = []

        with self.assertRaises(ValueError):
            crear_jugador(jugadores, "", 20, "Exterior")

        self.assertEqual(len(jugadores), 0)

    def test_modificacion_invalida(self):
        jugadores = [
            {"nombre": "Pol", "dorsal": 15, "posicion": "Exterior"},
            {"nombre": "Victor", "dorsal": 30, "posicion": "Exterior"}
        ]

        jugador = jugadores[0]

        with self.assertRaises(ValueError):
            actualizar_jugador(
                jugador,
                jugadores,
                nombre="Marc",
                dorsal=30
                )

        self.assertEqual(jugador["nombre"], "Pol")
        self.assertEqual(jugador["dorsal"], 15)
        self.assertEqual(jugador["posicion"], "Exterior")

if __name__ == "__main__":
    unittest.main()
