import unittest
from ejercicio_2 import parentesis_balanceados

class TestParentesisBalanceados(unittest.TestCase):

    def test_texto_balanceado(self):
        self.assertTrue(parentesis_balanceados("(hola)"))

    def test_texto_no_balanceado(self):
        self.assertFalse(parentesis_balanceados("((hola)"))

if __name__ == '__main__':
    unittest.main()
