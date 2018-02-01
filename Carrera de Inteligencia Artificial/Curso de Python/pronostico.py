import statistics as stats

metros_cuadrados_x = [5, 15, 20, 25]
precio_t = [375, 487, 450, 500]

cantidad_de_casas_n = 4

casa = int(raw_input('Ingresa el la cantidad de metros cuadrados para tu casa: '))

b1 = (375 * 5) + (487 * 15) + (450 * 20) + (500 * 25)
b2 = 375 + 487 + 450 + 500
b3 = 5 + 15 + 20 + 25
b4 = (5 ** 2) + (15 ** 2) + (20 ** 2) + (25 ** 2)
b5 = (5 + 15 + 20 + 25) ** 2

b_pendiente = (4 * b1) - (b2 * b3) / ((4 * b4) - b5)

a1 = stats.median(precio_t)
a2 = stats.median(metros_cuadrados_x)

a_interseccion = a1 - (b_pendiente * a2)

pronostico = a_interseccion + (b_pendiente * casa)

print('El resultado del pronostico para el precio de la casa que tu quieres adquirir es de: {}'.format(pronostico))
