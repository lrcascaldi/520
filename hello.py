#!/usr/bin/python3



# 2 notas
#INPUT

#historico = {'nota 1':n1,'nota 2':n2,'media notas':media}

#class Prova:
#
#    def __init__(self, n1, n2, media):
#        self.n1 = n1
#        self.n2 = n2
#
#    def media ():
#        media = (n1+n2)/2        

n1 = int(input("Digite a nota da P1: "))
n2 = int(input("Digite a nota da P2: "))

##PROCESS

media = (n1+n2)/2


##OUTPUT

geografia = Prova(7,5)


if media >= 7:
    print("Média {}.Aluno está aprovado!".format(media))
elif media > 3:
    print("Média {}.Aluno está em recuperação!".format(media))
else:
    print("Média {}.Aluno está reprovado!".format(media))

#print(historico)
