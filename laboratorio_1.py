num_int = 123
num_float = 3.14
texto_str = "hola"
booleano = True 

print (num_int, num_float, texto_str, booleano)

#Que Python tiene enteros sin límite se suele mostrar como una de sus
#bondades, es cierto. Yo no se por qué mi cerebro había interpolado la idea
#de que en float teníamos la misma ventaja.

#Justo estaba leyendo al respecto para entender bien y me quedó claro que no.
#Lo comparto:

#Tenemos floats de 64 bits por lo que el número más grande sería 1.8 * 10 ^
#308
#1.8 * 10 ** 308

n = int (input("Ingresar un numero"))
formula = (n+1) * n


print (formula)
