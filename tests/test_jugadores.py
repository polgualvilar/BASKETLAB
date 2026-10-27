
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from jugadores import crear_jugador, actualizar_jugador, borrar_jugador


class TestJugadores(unittest.TestCase):

    def setUp(self):
        self.jugadores = [
            {"nombre": "Pol", "dorsal": 15, "posicion": "Exterior"},
            {"nombre": "Victor", "dorsal": 30, "posicion": "Exterior"}
        ]

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

    def test_dorsal_negativo(self):
        jugadores = []
        
        with self.assertRaises(ValueError):
            crear_jugador(jugadores, "Pol", -20, "Exterior")
        
        self.assertEqual(len(jugadores), 0)

    def test_posicion_invalida(self):

        jugadores = []

        with self.assertRaises(ValueError):
            crear_jugador(jugadores, "Pol", 20, "Portero")
                
        self.assertEqual(len(jugadores), 0)

    def test_numero_jugadores(self):

        self.assertEqual(len(self.jugadores), 2)

    def test_modificar_nombre(self):

        actualizar_jugador(
            self.jugadores[0],
            self.jugadores,
            nombre="Marc"
        )

        self.assertEqual(self.jugadores[0]["nombre"], "Marc")
        self.assertEqual(self.jugadores[0]["dorsal"], 15)
        self.assertEqual(self.jugadores[0]["posicion"], "Exterior")

    def test_modificar_dorsal(self):

        actualizar_jugador(
            self.jugadores[0],
            self.jugadores,
            dorsal=23
        )

        self.assertEqual(self.jugadores[0]["nombre"], "Pol")
        self.assertEqual(self.jugadores[0]["dorsal"], 23)
        self.assertEqual(self.jugadores[0]["posicion"], "Exterior")

    def test_modificar_posicion(self):

        actualizar_jugador(
            self.jugadores[1],
            self.jugadores,
            posicion="Interior"
            )
        
        self.assertEqual(self.jugadores[1]["nombre"], "Victor")
        self.assertEqual(self.jugadores[1]["dorsal"], 30)
        self.assertEqual(self.jugadores[1]["posicion"], "Interior")

    def test_eliminar_jugador(self):

        self.assertEqual(len(self.jugadores), 2)

        borrar_jugador(
            self.jugadores,
            self.jugadores[0]
        )

        self.assertEqual(len(self.jugadores), 1)
        self.assertEqual(self.jugadores[0]["nombre"], "Victor")

    def test_eliminar_jugador_inexistente(self):

        jugador = {"nombre": "Marc", "dorsal": 99, "posicion": "Interior"},

        with self.assertRaises(ValueError):
            borrar_jugador(self.jugadores, jugador)

        self.assertEqual(len(self.jugadores), 2)

    def test_jugador_eliminado_devuelto(self):

        eliminado = borrar_jugador(self.jugadores, self.jugadores[0])

        self.assertEqual(len(self.jugadores), 1)
        self.assertEqual(eliminado["nombre"], "Pol")
                       

if __name__ == "__main__":
    unittest.main()
