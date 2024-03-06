# Desarrollar una función que reciba un texto e invierta el orden de las palabras siendo la
# última palabra la primera y la primera la última, debe devolver el texto invertido

def invertir_texto(texto):
    separado = texto.split()
    invertido = separado[::-1]
    texto_invertido = ' '.join(invertido)
    return texto_invertido

texto = 'espero pueda trabajar con ustedes <3'
resultado = invertir_texto(texto)
print(resultado)