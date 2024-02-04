"""
Problema 1:
Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
en el rango de 1500 y 2700 (ambos incluidos).
"""

numeros = []           #Creamos una lista para almacenar los datos
for numero in range(1500,2700):   #Verificamos si los números son divisibles  entre 7 y múltiplos de 5
    if numero %7==0 and numero%5==0:
        numeros.append(numero)    #Si cumple con lo anterior se agrega a la lista

print("Los números divisibles por 7 y múltiplos de 5, en el rango de 1500 y 2700, son: ")
print("")
print("Listado de números: ",numeros)

"""
Problema 2:
Escriba un programa en Python para construir el siguiente patrón.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
h = 5

for i in range(h):            #Establecemos el rango de h
    print('* ' * (i + 1))

for i in range(h - 1, 0, -1): #El rango será en decremento y empezará en h-1
    print('* ' * i)

"""
Problema 3:
Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
números.
Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
números pares e impares.
"""
numeros = []

while True:        #Usamos el True para crear un bucle que se detendrá hasta break
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").upper()
    if respuesta == "SI":
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)
    elif respuesta == "NO":
        break       #Cerramos el bucle
    else:
        print("Respuesta incorrecta. Ingrese SI o NO.")

print("Números ingresados:", numeros)

#Iniciamos contadores para las variables "par" e "impar"
par = 0
impar = 0

for numero in numeros:
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

print("Cantidad de números pares:", par)
print("Cantidad de números impares:", impar)

"""
Problema 4:
Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
materias.
"""
lista_de_alumnos = []
while True: #Ingresamos el nombre de los alumnos y creamos la lista notas
    nombre = input("Ingrese el nombre del alumno: ").upper()
    notas = []
    for j in range(3):
        while True:
            nota = float(input(f"Ingrese la nota {j + 1} del alumno {nombre}: "))
            if 0 <= nota <= 20:  #Las notas irán de 0 a 20
                notas.append(nota)
                break  
            else:
                print("Nota inválida, vuelva a intentar")

    alumno = {"Alumno": nombre, "Notas": notas}
    lista_de_alumnos.append(alumno)

    respuesta = input("¿Desea ingresar otro alumno? (SI/NO): ").upper()
    if respuesta != "SI":
        break

print("\nLista de alumnos y sus calificaciones:")
for alumno in lista_de_alumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")

"""
Problema 5:
Genere una función que tenga como parámetros el ingreso de un número entero y un dígito.
Verifique la cantidad de veces que se usa dicho número en el dígito solicitado.
"""
def contar_digitos(numero, digito):
    numero_str = str(numero) #Covertimos a cadena para usar el método count
    cantidad = numero_str.count(str(digito))
    return cantidad

num=int(input("Ingresa el número: "))
dig=int(input("El número que deseas contar es: "))
can_num=contar_digitos(num,dig)
print("La cantidad de veces que se repite el número ",dig," es: ", can_num)

"""
Problema 6:
Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
Nota: La secuencia de Fibonacci es la serie de números:
0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
Cada número siguiente se obtiene sumando los dos números anteriores.
"""
def fibonacci(limite):
    num1, num2 = 0, 1
    
    print(num1) # Mostramos el primer número

    while num2 <= limite: #Le establecemos un límite
        print(num2)
        num1, num2 = num2, num1 + num2

n=int(input("Ingrese el limite de la serie Fibonacci: "))
fibonacci(n)

"""
Problema 7
Escriba una función de Python que tome un número como parámetro y verifique que el número sea
primo o no.
"""
def Criba_de_Eratóstenes(numero):
    if numero < 2:
        return False
    
    #Se utiliza el método "Criba de Eratóstenes"
    for j in range(2, int(numero**0.5) + 1):
        if numero % j == 0:
            return False
    
    return True

num_cri = int(input("Inserte el número que desea comprobar: "))
if Criba_de_Eratóstenes(num_cri):
    print(num_cri, " es un número primo.")
else:
    print(num_cri, " no es un número primo.")
    
"""
Problema 8:
Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
función acepta el número como argumento
"""
def factorial(m):
# Condicionamos para que no se ejecute en negativos
    if m < 0:
        return "El factorial no está definido para números negativos."
    
    if m == 0:     # Factorial de 0 es 1
        return 1
    
    resultado = 1
    for i in range(1,m+1):
        resultado *= i
    
    return resultado

num_fac = int(input("Inserte el número que desea comprobar: "))
res = factorial(num_fac)
print("El factorial de ",num_fac, "es ", res)

"""
Problema 9:
Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio,
por ejemplo, omitiendo las vocales.
Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o
minúsculas.
Ejemplo:
- Input: Twitter Output: Twttr
- Input: What's your name? Output: Wht's yr nm?
"""
def omitir(cadena):
    vocales = "aeiouAEIOU"
    cadena_sin_vocales = ''.join(caracter for caracter in cadena if caracter not in vocales)
    return cadena_sin_vocales

entrada_usuario = input("Ingrese una cadena de texto: ")

resultado = omitir(entrada_usuario)
print("Texto original:", entrada_usuario)
print("Texto sin vocales:", resultado)

"""
Problema 10
En los Estados Unidos, las fechas suelen tener el siguiente formato: mes-día-año (MM/DD/AAAA). Las
fechas en ese formato no se pueden ordenar fácilmente porque el año de la fecha es el último en
lugar del primero. Intente ordenar, por ejemplo, 2/2/1800, 3/3/1900 y 1/1/2000 cronológicamente
en cualquier programa (por ejemplo, una hoja de cálculo). Las fechas en ese formato también son
ambiguas. ¡Una fecha como el 8 de septiembre de 1636, podría interpretarse como el 9 de agosto de
1636!
Implementar un programa que pida al usuario una fecha, en orden mes-día-año, con formato como
8/9/1636 o Septiembre 8, 1636, donde el mes en este último podría ser cualquiera de los valores en
la lista abajo:
[
"Enero",
"Febrero",
"Marzo",
"Abril",
"Mayo",
"Junio",
"Julio",
"Agosto",
"Septiembre",
"Octubre",
"Noviembre",
"Diciembre"
]
Luego, genere esa misma fecha en formato AAAA-MM-DD.
Ejemplos:
- Input: 9/8/1636 | Output: 1636-09-08
- Input: Septiembre 8, 1636 | Output: 1636-09-08
- Input: 1/1/1970 | Output: 1970-01-01
Nota:
- Los métodos de listas y string le resultarán de gran utilidad.
- Nota que si empleamos print(f"{n:02}") , esta completará con 0 valos a la izquierda de un
número
"""
def formatear_fecha(fecha):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril",
        "Mayo", "Junio", "Julio", "Agosto",
        "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]

    # Analizar la entrada en formato mes-día-año
    try:
        partes_fecha = fecha.split('/')
        if len(partes_fecha) == 3:
            mes, dia, anio = map(int, partes_fecha)
            return f"{anio:04d}-{mes:02d}-{dia:02d}"
    except ValueError:
        pass

    # Analizar la entrada en formato de palabras
    try:
        import dateutil.parser
        fecha_parseada = dateutil.parser.parse(fecha)
        return f"{fecha_parseada.year:04d}-{fecha_parseada.month:02d}-{fecha_parseada.day:02d}"
    except ValueError:
        pass

    return "No se reconoce el formato de fecha"


fecha = input("Ingrese una fecha (mes-día-año o formato de palabras): ")

resultado = formatear_fecha(fecha)
print(f"Fecha original: {fecha} | Fecha formateada: {resultado}")