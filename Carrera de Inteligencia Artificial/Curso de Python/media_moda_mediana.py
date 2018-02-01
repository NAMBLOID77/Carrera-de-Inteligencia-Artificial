import statistics as stats

#  -*- conding: utf-8 -*-

media = [1525, 257, 378, 9543, 7854, 152]
moda = [9, 5, 9, 4, 3, 6, 7, 1, 2, 3, 9, 1, 2]
mediana = [9, 5, 9, 4, 3, 6, 7, 1, 2, 3, 9, 1, 2]

print('Mean')
print(stats.mean(media))
print('Mode')
print(stats.mode(moda))
print('median')
print(stats.median(mediana))


