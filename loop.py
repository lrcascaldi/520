#!/usr/bin/python3

#from time import sleep
#
#x = 1
#
#num = int(input("Digite um número: "))
#
#while x < 10:
#    print("numero: {}".format(x))
#    x += 1
#    sleep(3)
#
#i = list(range(100,50,-2))

# letras = []

# for x in range (97, 97+26,1):
#     letras.append(chr(x))
# print(letras)


matriz = [
    [1, 3, 6],
    [3, 5, 7],
    [6, 9, 11]
]

a = 0
b = 0

for cont, x in enumerate(matriz):
    a += x[cont]
    b += x[-(cont+1)]
    cont += 1

print(a+b)


