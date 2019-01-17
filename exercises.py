#! /usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

def get_largest_number(numbers):
    """Gets the largest number from the list received.

    You CANNOT use `max` built-in method.

    :param numbers: List containing corresponding numbers
    :return: Largest number found
    """

    lista_numeros = []
    for i in range(0, len(numbers)):
        lista_numeros.append(numbers[i])

    lista_numeros.sort()
    return lista_numeros[len(numbers)-1]


def get_smallest_number(numbers):
    """Gets the smallest number from the list received.

    You CANNOT use `min` built-in method.

    :param numbers: List containing corresponding numbers
    :return: Smallest number found
    """
    lista_numeros = []
    for i in range(0, len(numbers)):
       lista_numeros.append(numbers[i])

    # x = 0
    # for element in numbers:
    #     print "{}.-{}".format(x, numbers[x])
    #     x += 1

    lista_numeros.sort()
    return lista_numeros[0]


def get_even_numbers(numbers):
    """Gets all even numbers from the list received.

    This function MUST NOT modify the received `numbers` list.

    :param numbers: - List containing corresponding numbers
    :return: New list containing all even numbers found
    """
    #pass  # <--- remove this `pass` and put your code here
    lista_numeros = []
    los_numeros_pares = []
    numero_intermedio = None

    for i in range(0, len(numbers)):
        lista_numeros.append(numbers[i])

    lista_numeros.sort()

    for element in lista_numeros:
        numero_intermedio = element % 2
        if numero_intermedio == 0:
            los_numeros_pares.append(element)
    return los_numeros_pares


def filter_even_numbers(numbers):
    """Filters even numbers in the list received.

    This function MUST modify the received `numbers` list.

    :param numbers: List containing corresponding numbers
    :return: Nothing
    """
    lista_numeros = []

    for element in numbers:
        lista_numeros.append(element)

    for element in lista_numeros:
        if not element%2 == 0:
            numbers.pop(numbers.index(element))

    #numbers.sort()


def draw_solid_rectangle(x, y):
    """Generates a string with a solid rectangle made of * symbols with `x` columns and `y` rows.

    :param x: Number of columns (width)
    :param y: Number of rows (height)
    :return: String containing corresponding solid rectangle
    """
    dibujo = ""
    for a in range(y):
        for b in range(x):
            dibujo = dibujo + "*"
            if b==x-1:
                if not a == y-1:
                    dibujo = dibujo + "\n"
    return dibujo


def draw_rectangle_borders(x, y):
    """Generates a string with a rectangle borders made of * symbols with `x` columns and `y` rows.

    :param x: Number of columns (width)
    :param y: Number of rows (height)
    :return: String containing corresponding rectangle border
    """
    dibujo = ""
    espacio = " "
    asterisco = "*"
    salto_linea= "\n"
    for a in range(1, y+1):
        for b in range(1, x+1):
            if a == 1 or a == y:
                dibujo = dibujo + asterisco
            elif b == 1 or b == x:
                dibujo = dibujo + asterisco
            else:
                dibujo = dibujo + espacio

        if not a == y:
            dibujo= dibujo + salto_linea
    return dibujo


def draw_pyramid(height):
    """Generates a string with a pyramid made of * symbols and `height` rows.

    :param height: Number of rows (height)
    :return: String containing corresponding pyramid
    """
    dibujo_triangulo = ""
    espacio = ""
    asterisco = ""
    salto_linea = "\n"

    for numero_linea in range(height):
        espacio = height - numero_linea - 1
        asterisco = 1 + numero_linea * 2
        dibujo_triangulo = dibujo_triangulo + " " * espacio
        dibujo_triangulo = dibujo_triangulo + "*" * asterisco

        if not numero_linea == height-1:
            dibujo_triangulo = dibujo_triangulo + salto_linea

    return dibujo_triangulo


def draw_inverted_pyramid(height):
    """Generates a string with a inverted pyramid made of * symbols and `height` rows.

    :param height: Number of rows (height)
    :return: String containing corresponding inverted pyramid
    """
    dibujo_triangulo_invertido = ""
    for linea in range(height):
        asterisco = height * 2 - linea * 2 -1
        espacio = linea + 1
        dibujo_triangulo_invertido = dibujo_triangulo_invertido + " " * linea
        dibujo_triangulo_invertido = dibujo_triangulo_invertido + "*" * asterisco

        if not linea == height-1:
            dibujo_triangulo_invertido = dibujo_triangulo_invertido + "\n"
    return dibujo_triangulo_invertido


def chars_counter(string):
    """Counts number of times each char appears in a string.

    You CANNOT use `collections.Counter` class.

    Note that uppercase and lowercase are different letters (e.g. 'A' is different from 'a')

    :param string: String to count chars
    :return: Dictionary with char and counter key-value pairs
    """
    lista_del_texto = []
    contador = {}
    for i in range(len(string)):
        lista_del_texto.append(string[i])

    for x in range(len(string)):
        letra = string[x]
        contador.setdefault(letra, lista_del_texto.count(letra))

    return contador


def sort_list_ascending(elements):
    """Sorts list received in a new list with ascending order.

    You CANNOT use `sorted` built-in method.

    :param elements: List of elements to be sorted
    :return: New list with elements sorted
    """

    lista = []

    for elementos in elements:
        lista.append(elementos)
    lista.sort()

    return lista

def check_date(day, month, year):
    """Checks if received date is valid or not.

    You CANNOT use `datetime` nor `calendar` modules

    Be careful with leap years ;)

    :param day: Day number
    :param month: Month number
    :param year: Year number
    :return: True if date is valid, False otherwise
    """
    es_year_bisiesto = False
    fecha_correcta = False

    if year > 0:
        if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
            es_year_bisiesto = True

        if (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12):
            if (day > 0) and (day <= 31):
                fecha_correcta = True
        elif (month == 4) or (month == 6) or (month ==  9) or (month == 11):
            if (day > 0) and (day <= 30):
                fecha_correcta = True
        elif month == 2:
            if es_year_bisiesto:
                if (day > 0) and (day <= 29):
                    fecha_correcta = True
            else:
                if (day > 0) and (day <= 28):
                    fecha_correcta = True


    return fecha_correcta


def check_palindrome(string):
    """Checks if received string is palindrome or not.

    Be careful with white spaces, special symbols, lowercase and uppercase ;)

    :param string: String to be checked
    :return: True if string is palindrome, False otherwise
    """
    ordenado = []
    reves = []

    for i in range(len(string)):
        ordenado.append(string[i].upper())
        reves.append(string[i].upper())
    reves.reverse()
    texto1 = reves.__str__()
    print texto1


def join_strings(strings):
    """Concatenates a list of words with intervening occurrences of comma.

    You CANNOT use `str.join` method.

    :param strings: List of strings to be concatenated
    :return: Concatenated string
    """
    pass  # <--- remove this `pass` and put your code here


def pinto_monas():
    # --- Parte 3 ---
    # Pedimos el lado
    lado = int(raw_input("Lado: "))

    # Definimos una variable para dibujar los espacios
    espacios = lado - 1
    for i in range(lado, 3 * lado, 2):
        print " " * espacios + "*" * i
        espacios -= 1

    espacios = 1
    for i in range(3 * lado - 4, lado - 2, -2):
        print " " * espacios + "*" * i
        espacios += 1


if __name__ == '__main__':
    # if you need to execute custom code to check results, do it here!
    #pass
    numeros_lista = []
    num = []
    for i in range(0, 8):
        numeros_lista.append(randint(1, 1000))
        num.append(randint(1, 100))

    print
    print "Lista generada es:\n{}\n".format(numeros_lista)
    print ".-El numero mas grande es: {}".format(get_largest_number(numeros_lista))
    print ".-El número más pequeño es: {}".format(get_smallest_number(numeros_lista))
    print ".-Los numeros pares son: {}".format(get_even_numbers(numeros_lista))
    filter_even_numbers(numeros_lista)
    print ".-Imprimimos un recuadro solido con '*': \n{}".format(draw_solid_rectangle(
        randint(1, 10),
        randint(1, 10)
    ))
    print "Imprimimos un recuadro solo su borde: \n{}".format(draw_rectangle_borders(
        randint(1, 10),
        randint(1, 10)
    ))
    numero = randint(1, 10)
    print "Imprimimos un triangulo con '*' de {} lineas: \n{}".format(numero, draw_pyramid(numero))
    print "Imprimimos un triangulo invertido con '*' de {} líneas: \n{}".format(numero, draw_inverted_pyramid(numero))
    #print "Pinto monas: {}".format(pinto_monas())
    frase = raw_input("Introduzca una frase: ")
    print "Imprimimos el conteo de letras de la frase introducida: \n{}".format(chars_counter(frase))
    print "Ordenamosla lista generada anteriormente {}: \n{}".format(num, sort_list_ascending(num))
    print "Introduzca una fecha: "
    dia = int(raw_input(".-Introduzca el día: "))
    mes = int(raw_input(".-Introduzca el mes: "))
    year = int(raw_input(".-Introduzca el año: "))
    print "¿Es correcta la fecha?: {}".format(check_date(dia, mes, year))
    print "Palindromo: {}".format(check_palindrome("cateto"))