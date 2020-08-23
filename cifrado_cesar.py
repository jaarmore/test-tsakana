#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Escribe una función que, dado un mensaje cifrado y un desplazamiento,
calcule y devuelva el mensaje original.
"""


def cifrado_cesar(mensaje_cifrado, desplazamiento):
    """Funcion que toma un mensaje cifrado y un desplazamiento
       y devuelve el mensaje original

    Args:
        mensaje_cifrado ([String]): [mensaje cifrado]
        desplazamiento ([integer]): [numero de caracteres a desplazar]

    Returns:
        [String]: [el mesaje original o descifrado]
    """
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    mensaje_original = ''
    desplazamiento = desplazamiento * -1

    for caracter in mensaje_cifrado:
        if caracter.isalpha():
            posicion = alfabeto.index(caracter)
            posicion += desplazamiento

            if posicion > len(alfabeto) - 1:
                posicion -= 27
            elif posicion < 0:
                posicion += 27
            mensaje_original += alfabeto[posicion]
    return mensaje_original
