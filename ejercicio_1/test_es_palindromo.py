import unittest
from ejercicio_1 import es_palindromo

class TestEsPalindromo(unittest.TestCase):

    def test_palabra_palindromo(self):
        self.assertTrue(es_palindromo("reconocer"))

    def test_palabra_no_palindromo(self):
        self.assertFalse(es_palindromo("Hola"))

if __name__ == '__main__':
    unittest.main()