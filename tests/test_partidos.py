
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from partidos import crear_partido, registrar_partido, agregar_partido


class TestPartidos(unittest.TestCase):

    # ==========================================
    # 1. CREACIÓN DE PARTIDOS
    # ==========================================

    def test_crear_partido(self):
        partido = crear_partido(
            id=1,
            rival="Rival Team",
            fecha="15/06/2024",
            lugar="Local",
            puntos_favor=80,
            puntos_contra=75
        )

        self.assertEqual(partido["id"], 1)
        self.assertEqual(partido["rival"], "Rival Team")
        self.assertEqual(partido["fecha"], "15/06/2024")
        self.assertEqual(partido["lugar"], "Local")
        self.assertEqual(partido["puntos_favor"], 80)
        self.assertEqual(partido["puntos_contra"], 75)

    # ==========================================
    # 2. VALIDACIÓN DEL ID
    # ==========================================

    def test_crear_partido_id_valido(self):
        ids_validos = [0, 1, 15, 100]

        for id_partido in ids_validos:
            with self.subTest(id=id_partido):
                partido = crear_partido(
                    id=id_partido,
                    rival="Basket Terrassa",
                    fecha="07/11/2026",
                    lugar="Local",
                    puntos_favor=65,
                    puntos_contra=58
                )

                self.assertEqual(partido["id"], id_partido)

    def test_crear_partido_id_invalido(self):
        ids_invalidos = [-1, "1", True, 3.5, None]

        for id_partido in ids_invalidos:
            with self.subTest(id=id_partido):
                with self.assertRaises(ValueError):
                    crear_partido(
                        id=id_partido,
                        rival="Basket Terrassa",
                        fecha="07/11/2026",
                        lugar="Local",
                        puntos_favor=65,
                        puntos_contra=58
                    )

    def test_id_duplicado(self):
        partidos = [
            {"id": 1, "rival": "Basket Terrassa"},
            {"id": 2, "rival": "Sabadell Basket"}
        ]

        partido = crear_partido(
            id=2,
            rival="Rival Team",
            fecha="07/11/2026",
            lugar="Local",
            puntos_favor=80,
            puntos_contra=75
        )

        with self.assertRaises(ValueError):
            registrar_partido(partidos, partido)

        self.assertEqual(len(partidos), 2)

    # ==========================================
    # 3. VALIDACIÓN DEL RIVAL
    # ==========================================

    def test_crear_partido_rival_valido(self):
        partido = crear_partido(
            id=1,
            rival="  Basket Terrassa  ",
            fecha="07/11/2026",
            lugar="Local",
            puntos_favor=65,
            puntos_contra=58
        )

        self.assertEqual(partido["rival"], "Basket Terrassa")

    def test_crear_partido_rival_invalido(self):
        rivales_invalidos = ["", "   ", 123, None, True]

        for rival in rivales_invalidos:
            with self.subTest(rival=rival):
                with self.assertRaises(ValueError):
                    crear_partido(
                        id=1,
                        rival=rival,
                        fecha="07/11/2026",
                        lugar="Local",
                        puntos_favor=65,
                        puntos_contra=58
                    )

    # ==========================================
    # 4. VALIDACIÓN DE LA FECHA
    # ==========================================

    def test_crear_partido_fecha_valida(self):
        partido = crear_partido(
                    id=1,
                    rival="Basket Terrassa",
                    fecha="28/10/2026",
                    lugar="Local",
                    puntos_favor=65,
                    puntos_contra=58
                )

        self.assertEqual(partido["fecha"], "28/10/2026")

    def test_crear_partido_fecha_invalida(self):
        fechas_invalidos = ["31/02/2026", "32/10/2026", "28/13/2026", "2026-10-28", "5/1/2026", "", 28102026, None]
        
        for fechas in fechas_invalidos:
            with self.subTest(fechas=fechas):
                with self.assertRaises(ValueError):
                    crear_partido(
                        id=1,
                        rival="Basket Terrassa",
                        fecha=fechas,
                        lugar="Local",
                        puntos_favor=65,
                        puntos_contra=58
                    )

    # ==========================================
    # 5. VALIDACIÓN DEL LUGAR
    # ==========================================

    def test_crear_partido_lugar_valido(self):
        partido = crear_partido(
            id=1,
            rival="Basket Terrassa",
            fecha="28/10/2026",
            lugar="local",
            puntos_favor=65,
            puntos_contra=58
        )

        self.assertEqual(partido["lugar"], "Local")

    def test_crear_partido_lugar_invalido(self):
        lugares_invalidos = ["Neutral", "Casa", "", 123, None]

        for lugar in lugares_invalidos:
                    with self.subTest(lugar=lugar):
                        with self.assertRaises(ValueError):
                            crear_partido(
                                id=1,
                                rival="Basket Terrassa",
                                fecha="15/01/2026",
                                lugar=lugar,
                                puntos_favor=65,
                                puntos_contra=58
                            )
    # ==========================================
    # 6. VALIDACIÓN DE PUNTUACIONES
    # ==========================================

    # Próximas pruebas:
    def test_crear_partido_puntos_validos(self):
        
        casos = [
            (0, 0),
            (65, 58),
            (100, 99)
        ]

        for favor, contra in casos:
            with self.subTest(favor=favor, contra=contra):
                partido = crear_partido(
                    id=1,
                    rival="Basket Terrassa",
                    fecha="28/10/2026",
                    lugar="Local",
                    puntos_favor=favor,
                    puntos_contra=contra
                )

                self.assertEqual(partido["puntos_favor"], favor)
                self.assertEqual(partido["puntos_contra"], contra)

    def test_crear_partido_puntos_invalidos(self):

        casos_invalidos = [
            (-1, 50),
            (60, -1),
            ("80", 70),
            (80, True),
            (3.5, 60),
            (60, None)
        ]

        for favor, contra in casos_invalidos:
            with self.subTest(favor=favor, contra=contra):
                with self.assertRaises(ValueError):
                    crear_partido(
                        id=1,
                        rival="Basket Terrassa",
                        fecha="15/01/2026",
                        lugar="Local",
                        puntos_favor=favor,
                        puntos_contra=contra
                    )

    # ==========================================
    # 7. REGISTRO DE PARTIDOS
    # ==========================================

    def test_registrar_partido(self):
        partidos = []

        partido = crear_partido(
            id=1,
            rival="Basket Terrassa",
            fecha="07/11/2026",
            lugar="Local",
            puntos_favor=65,
            puntos_contra=58
        )

        registrado = registrar_partido(partidos, partido)

        self.assertEqual(len(partidos), 1)
        self.assertIn(partido, partidos)
        self.assertEqual(registrado, partido)

    # ==========================================
    # 8. AGREGAR PARTIDOS
    # ==========================================
    def test_agregar_partido(self):

        partidos = []

        entradas = [
            "1",
            "Basket Terrassa",
            "28/10/2026",
            "Local",
            "65",
            "58"
        ]

        with patch("builtins.input", side_effect=entradas):
            agregar_partido(partidos)

        self.assertEqual(len(partidos), 1)
        self.assertEqual(partidos[0]["id"], 1)
        self.assertEqual(partidos[0]["rival"], "Basket Terrassa")
        self.assertEqual(partidos[0]["fecha"], "28/10/2026")
        self.assertEqual(partidos[0]["lugar"], "Local")
        self.assertEqual(partidos[0]["puntos_favor"], 65)
        self.assertEqual(partidos[0]["puntos_contra"], 58)

    
    def test_agregar_partido_id_duplicado(self):

        partidos = [
            {
                "id": 1,
                "rival": "Basket Terrassa",
                "fecha": "28/10/2026",
                "lugar": "Local",
                "puntos_favor": 65,
                "puntos_contra": 58
            }
        ]

        entradas = [
            "1",
            "Sabadell Basket",
            "29/10/2026",
            "Visitante",
            "70",
            "60"
        ]

        with patch("builtins.input", side_effect=entradas):
            agregar_partido(partidos)

        self.assertEqual(len(partidos), 1)
        self.assertEqual(partidos[0]["id"], 1)
        self.assertEqual(partidos[0]["rival"], "Basket Terrassa")
        self.assertEqual(partidos[0]["puntos_favor"], 65)
        self.assertEqual(partidos[0]["puntos_contra"], 58)

    # ==========================================
    # 9. CONSULTA DE PARTIDOS
    # ==========================================

    # Aquí añadiremos futuras pruebas de búsqueda.

    # ==========================================
    # 10. MODIFICACIÓN DE PARTIDOS
    # ==========================================

    # Aquí añadiremos futuras pruebas de modificación.

    # ==========================================
    # 12. ELIMINACIÓN DE PARTIDOS
    # ==========================================

    # Aquí añadiremos futuras pruebas de eliminación.


if __name__ == "__main__":
    unittest.main()
