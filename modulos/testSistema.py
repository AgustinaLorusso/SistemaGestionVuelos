import unittest
from gestionAsientos import reservar_asiento
from gestionPasajeros import validar_password, buscar_pasajero_por_dni


class TestSistema(unittest.TestCase):

    # ALTAS CORRECTAS

    def test_estructura_pasajero_valida(self):
        pasajero = [
            "mar123",
            "Mar Lopez",
            "12345678",
            "mar@gmail.com",
            "hash",
            0
        ]

        self.assertEqual(len(pasajero), 6)
        self.assertEqual(pasajero[0], "mar123")
        self.assertEqual(pasajero[2], "12345678")

    # BÚSQUEDAS

    def test_busqueda_pasajero_existente(self):
        pasajero = buscar_pasajero_por_dni("43903033")

        self.assertIsNotNone(pasajero)
        self.assertEqual(pasajero[2], "43903033")

    # VALIDACIONES

    def test_password_valida(self):
        self.assertTrue(validar_password("Clave123"))

    def test_password_invalida(self):
        self.assertFalse(validar_password("123"))

    # CÁLCULOS / OPERACIONES DEL SISTEMA

    def test_reservar_asiento_libre(self):
        matriz = [
            ["D", "D"],
            ["D", "D"]
        ]

        resultado = reservar_asiento(matriz, 1, 1)

        self.assertTrue(resultado)
        self.assertEqual(matriz[0][0], "R")

    def test_asiento_ocupado(self):
        matriz = [
            ["R", "D"],
            ["D", "D"]
        ]

        resultado = reservar_asiento(matriz, 1, 1)

        self.assertFalse(resultado)

    def test_asiento_fuera_de_rango(self):
        matriz = [
            ["D", "D"],
            ["D", "D"]
        ]

        resultado = reservar_asiento(matriz, 10, 10)

        self.assertFalse(resultado)


if __name__ == "__main__":
    unittest.main()