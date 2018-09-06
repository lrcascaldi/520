
from random import random

numeros = [12, 45, 212, 4321, 23432, 54, 5321, 11]

#forma com list compherension com if ternario

par = [x for x in numeros if x % 2 == 0]

#outra forma mais simples abaixo

#par = []
#
#for x in numeros:
#    if x % 2 == 0:
#        par.append(x)

print(par)




