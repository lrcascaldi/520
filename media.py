#!/usr/bin/python3

notas = int(input("Digite número de notas: "))

soma = 0

for x in range (notas):
    nota = int(input("digite n{}: ".format(x+1)))
    soma += nota
media = soma / notas

#saida

if media >= 7:
    print("Média {} .Aluno está aprovado!".format(media))
elif media > 3:
    print("Média {} .Aluno está em recuperação!".format(media))
else:
    print("Média {} .Aluno está reprovado!".format(media))

