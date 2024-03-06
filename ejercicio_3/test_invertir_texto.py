import unittest
from ejercicio_3 import invertir_texto

class TestInvertirTexto(unittest.TestCase):

    def test_invertir_texto(self):
        texto = 'espero pueda trabajar con ustedes <3'
        resultado_esperado = '<3 ustedes con trabajar pueda espero'
        self.assertEqual(invertir_texto(texto), resultado_esperado)

if __name__ == '__main__':
    unittest.main()
