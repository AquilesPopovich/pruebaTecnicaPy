# Desarrollar una función que reciba una palabra y devuelva True en caso de ser un
# palíndromo y False en caso de no serlo

def es_palindromo(palabra):

    palabra = palabra.lower()

    return palabra == palabra[::-1]

palabra = "hola"
resultado = es_palindromo(palabra)
print(resultado)