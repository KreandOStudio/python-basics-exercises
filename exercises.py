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
        #print "{}.-{}".format(i, lista_numeros[i])

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
    for a in range(y):
        for b in range(x):
            if a == 1:
                dibujo = dibujo + asterisco
            if a == y:
                dibujo = dibujo + asterisco
            if b == 1:
                dibujo = dibujo + asterisco
            if b == x:
                dibujo = dibujo + asterisco

            dibujo = dibujo + espacio

        dibujo= dibujo + salto_linea
    return dibujo


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


def draw_pyramid(height):
    """Generates a string with a pyramid made of * symbols and `height` rows.

    :param height: Number of rows (height)
    :return: String containing corresponding pyramid
    """
    pass  # <--- remove this `pass` and put your code here


def draw_inverted_pyramid(height):
    """Generates a string with a inverted pyramid made of * symbols and `height` rows.

    :param height: Number of rows (height)
    :return: String containing corresponding inverted pyramid
    """
    pass  # <--- remove this `pass` and put your code here


def chars_counter(string):
    """Counts number of times each char appears in a string.

    You CANNOT use `collections.Counter` class.

    Note that uppercase and lowercase are different letters (e.g. 'A' is different from 'a')

    :param string: String to count chars
    :return: Dictionary with char and counter key-value pairs
    """
    pass  # <--- remove this `pass` and put your code here


def sort_list_ascending(elements):
    """Sorts list received in a new list with ascending order.

    You CANNOT use `sorted` built-in method.

    :param elements: List of elements to be sorted
    :return: New list with elements sorted
    """
    pass  # <--- remove this `pass` and put your code here


def check_date(day, month, year):
    """Checks if received date is valid or not.

    You CANNOT use `datetime` nor `calendar` modules

    Be careful with leap years ;)

    :param day: Day number
    :param month: Month number
    :param year: Year number
    :return: True if date is valid, False otherwise
    """
    pass  # <--- remove this `pass` and put your code here


def check_palindrome(string):
    """Checks if received string is palindrome or not.

    Be careful with white spaces, special symbols, lowercase and uppercase ;)

    :param string: String to be checked
    :return: True if string is palindrome, False otherwise
    """
    pass  # <--- remove this `pass` and put your code here


def join_strings(strings):
    """Concatenates a list of words with intervening occurrences of comma.

    You CANNOT use `str.join` method.

    :param strings: List of strings to be concatenated
    :return: Concatenated string
    """
    pass  # <--- remove this `pass` and put your code here


if __name__ == '__main__':
    # if you need to execute custom code to check results, do it here!
    #pass
    numeros_lista = []
    for i in range(0, 8):
        numeros_lista.append(randint(1, 1000))

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
    print "Pinto monas: {}".format(pinto_monas())
