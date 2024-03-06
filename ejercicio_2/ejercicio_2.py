# Desarrollar una función que reciba un texto e identifique que todos los paréntesis estén
# balanceados (chequear que siempre que se abra un paréntesis este se cierre), devolver
# True caso que así sea, False caso contrario

def parentesis_balanceados(texto):
    parentesis = []
    for caracter in texto:
        if caracter == '(':
            parentesis.append(caracter)
        elif caracter == ')':
            if not parentesis or parentesis.pop() != '(':
                return False
    return not parentesis


texto = "((hola)"
resultado = parentesis_balanceados(texto)
print(resultado)