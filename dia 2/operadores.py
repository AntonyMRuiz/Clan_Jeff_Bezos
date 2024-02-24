# Operadores

# operadores logicos

# And "y"
condicionalAnd = False and True
# print(not condicionalAnd)

# Or "o"
condicionalOr = not ((1 < 2) or (12 >= 2))
# print(not condicionalOr)

# not "contrario"
condicionalNot = not False
# print(not condicionalNot)

# == "Es igual"
esigual = "Jhonatan" == "jhonatan"
# print(esigual)

# != Diferente
esDiferente = 12 != 12.0
# print(esDiferente)

# operadores de comparacion

# > "Mayor que"
comparadorNum = 1 > 2
# print(comparadorNum)

# < "Menor que"
comparadorNum = 5 < 8
# print(comparadorNum)

# <= "Menor que O igual"
comparadorNum = 5 <= 3
# print(comparadorNum)

# <= "Mayor que O igual"
comparadorNum = 5 >= 3
print(comparadorNum)


"""
Crear 2 variables numericas de cualquier tipo
y realizar las operaciones aritmeticas basicas
y almacenar ese resultado en una variable que se llame
result e imprimir en consola los resultados
(+ - / // * ** %)
""" 

# Declarar las 2 variables con valores numericos
numeroUno = 15
numeroDos = 2

# operaciones basicas
# suma
result = numeroUno + numeroDos
print("La suma de los numeros es:" , result)

# resta
result = numeroUno - numeroDos
print("La resta de los numeros es:" ,result)

# division 
result = numeroUno / numeroDos
print("La division de los numeros es:" ,result)

# division entera
result = numeroUno // numeroDos
print("La division entera de los numeros es:" ,result)

# multiplicacion
result = numeroUno * numeroDos
print("La multiplicacion de los numeros es:" ,result)

# exponecial
result = numeroUno ** numeroDos
print(f"La suma de  es: ", result)

# modulo
result = numeroUno % numeroDos
print(f"""----------------------
El modulo de la division 
de {numeroUno} % {numeroDos} 
es: {result}
---------------------------""")