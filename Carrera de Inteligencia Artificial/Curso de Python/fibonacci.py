# -*- coding: utf-8 -*-

ingreso = int(raw_input('Ingrese un número: '))
numero = 1
ultimo = 0
penultimo = 0

print(numero)

for conteo in range(ingreso):

    penultimo = ultimo
    ultimo = numero
    numero = penultimo + ultimo

    print(numero)
