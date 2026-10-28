
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from api import app


class TestAPI(unittest.TestCase):


    def setUp(self):
        self.cliente = TestClient(app)


    def test_inicio(self):
        respuesta = self.cliente.get("/")

        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(
            respuesta.json(),
            {"mensaje": "Bienvenido a BasketLab"}
        )

    def test_obtener_jugadores(self):

        jugadores_prueba = [
            {
                "nombre": "Pol",
                "dorsal": 15,
                "posicion": "Exterior"
            },
            {
                "nombre": "Victor",
                "dorsal": 30,
                "posicion": "Exterior"
            }
        ]

        with patch("api.cargar_jugadores", return_value=jugadores_prueba):
            respuesta = self.cliente.get("/jugadores")

        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.json(), jugadores_prueba)

    def test_obtener_jugador_por_dorsal(self):

        jugadores_prueba = [
            {
                "nombre": "Jugador Prueba",
                "dorsal": 15,
                "posicion": "Exterior"
            }
        ]

        with patch("api.cargar_jugadores", return_value=jugadores_prueba):
            respuesta = self.cliente.get("/jugadores/15")

        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.json(), jugadores_prueba[0])

    def test_obtener_jugador_dorsal_inexistente(self):

        jugadores_prueba = [
            {
                "nombre": "Jugador Prueba",
                "dorsal": 15,
                "posicion": "Exterior"
            }
        ]

        with patch("api.cargar_jugadores", return_value=jugadores_prueba):
            respuesta = self.cliente.get("/jugadores/99")

        self.assertEqual(respuesta.status_code, 404)
        self.assertEqual(
            respuesta.json(),
            {"detail": "Jugador no encontrado"}
        )

    def test_obtener_partidos(self):

        partidos_prueba = [
            {
                "id": 1,
                "rival": "Basket Terrassa",
                "fecha": "28/10/2026",
                "lugar": "Local",
                "puntos_favor": 65,
                "puntos_contra": 58
            },
            {
                "id": 2,
                "rival": "Sabadell Basket",
                "fecha": "29/10/2026",
                "lugar": "Visitante",
                "puntos_favor": 70,
                "puntos_contra": 62
            }
        ]

        with patch("api.cargar_partidos", return_value=partidos_prueba):
            respuesta = self.cliente.get("/partidos")

        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.json(), partidos_prueba)

    # ==========================================
    # 6. REGISTRO DE JUGADORES
    # ==========================================

    def test_registrar_jugador(self):

        jugadores_prueba = []

        nuevo_jugador = {
            "nombre": "Marc",
            "dorsal": 23,
            "posicion": "Exterior"
        }

        with patch("api.cargar_jugadores", return_value=jugadores_prueba), \
            patch("api.guardar_jugadores") as guardar_mock:

            respuesta = self.cliente.post(
                "/jugadores",
                json=nuevo_jugador
            )

        self.assertEqual(respuesta.status_code, 201)
        self.assertEqual(respuesta.json(), nuevo_jugador)
        self.assertEqual(jugadores_prueba, [nuevo_jugador])
        guardar_mock.assert_called_once_with(jugadores_prueba)

    def test_registrar_jugador_nombre_invalido(self):

        jugadores_prueba = []

        nuevo_jugador = {
            "nombre": "",
            "dorsal": 23,
            "posicion": "Exterior"
        }

        with patch("api.cargar_jugadores", return_value=jugadores_prueba), \
            patch("api.guardar_jugadores") as guardar_mock:
        
            respuesta = self.cliente.post(
                "/jugadores",
                json=nuevo_jugador
            )

        self.assertEqual(respuesta.status_code, 400)
        self.assertEqual(jugadores_prueba, [])
        guardar_mock.assert_not_called()


    def test_registrar_jugador_dorsal_duplicado(self):

        jugadores_prueba = [
            {
                "nombre": "Pol",
                "dorsal": 15,
                "posicion": "Exterior"
            }
        ]

        nuevo_jugador = {
            "nombre": "Marc",
            "dorsal": 15,
            "posicion": "Interior"
        }

        with patch("api.cargar_jugadores", return_value=jugadores_prueba), \
            patch("api.guardar_jugadores") as guardar_mock:

            respuesta = self.cliente.post(
                "/jugadores",
                json=nuevo_jugador
            )

        self.assertEqual(respuesta.status_code, 400)
        self.assertEqual(len(jugadores_prueba), 1)
        self.assertEqual(jugadores_prueba[0]["nombre"], "Pol")
        guardar_mock.assert_not_called()

    def test_registrar_jugador_dorsal_invalida(self):
    
            jugadores_prueba = []
    
            nuevo_jugador = {
                "nombre": "Marc",
                "dorsal": "hola",
                "posicion": "Exterior"
            }
    
            with patch("api.cargar_jugadores", return_value=jugadores_prueba), \
                patch("api.guardar_jugadores") as guardar_mock:
            
                respuesta = self.cliente.post(
                    "/jugadores",
                    json=nuevo_jugador
                )
    
            self.assertEqual(respuesta.status_code, 422)
            self.assertEqual(jugadores_prueba, [])
            guardar_mock.assert_not_called()

    def test_registrar_jugador_posicion_invalida(self):

        jugadores_prueba = []

        nuevo_jugador = {
            "nombre": "Marc",
            "dorsal": 23,
            "posicion": "Portero"
        }

        with patch("api.cargar_jugadores", return_value=jugadores_prueba), \
            patch("api.guardar_jugadores") as guardar_mock:
        
            respuesta = self.cliente.post(
                "/jugadores",
                json=nuevo_jugador
            )

        self.assertEqual(respuesta.status_code, 400)
        self.assertEqual(jugadores_prueba, [])
        guardar_mock.assert_not_called()

    def test_registrar_partido_api(self):
        partidos_prueba = []

        nuevo_partido = {
            "id": 1,
            "rival": "Basket Terrassa",
            "fecha": "28/10/2026",
            "lugar": "Local",
            "puntos_favor": 65,
            "puntos_contra": 58
        }

        with patch("api.cargar_partidos", return_value=partidos_prueba), \
            patch("api.guardar_partidos") as guardar_mock:

            respuesta = self.cliente.post(
                "/partidos",
                json=nuevo_partido
                )

        self.assertEqual(respuesta.status_code, 201)
        self.assertEqual(respuesta.json(), nuevo_partido)
        self.assertEqual(partidos_prueba, [nuevo_partido])
        guardar_mock.assert_called_once_with(partidos_prueba)

    def test_registrar_partido_api_id_duplicado(self):

        partidos_prueba = [
            {
                "id": 1,
                "rival": "Basket Terrassa",
                "fecha": "28/10/2026",
                "lugar": "Local",
                "puntos_favor": 65,
                "puntos_contra": 58
            }
        ]
        
        nnuevo_partido = {
            "id": 1,
            "rival": "Sabadell Basket",
            "fecha": "29/10/2026",
            "lugar": "Visitante",
            "puntos_favor": 70,
            "puntos_contra": 65
        }
        
        with patch("api.cargar_partidos", return_value=partidos_prueba), \
            patch("api.guardar_partidos") as guardar_mock:
        
            respuesta = self.cliente.post(
                "/partidos",
                json=nnuevo_partido
            )
        
        self.assertEqual(respuesta.status_code, 400)
        self.assertEqual(len(partidos_prueba), 1)
        self.assertEqual(partidos_prueba[0]["id"], 1)
        self.assertEqual(partidos_prueba[0]["rival"], "Basket Terrassa")
        guardar_mock.assert_not_called()

            


    



if __name__ == "__main__":
    unittest.main()
