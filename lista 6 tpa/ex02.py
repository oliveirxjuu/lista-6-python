# Escreva um algoritmo que leia dois números inteiros e exiba a
#  multiplicação entre eles se o primeiro número for par; caso contrário, exiba a soma dos números. 

num1 = int(input("Digite um número: "))
num2 = int(input("Digitie outro número: "))

rep = num1 % 2
if rep == 0:
    mult = num1 * num2
    print(f"{mult}")
else:
    soma = num1 + num2
    print(f"{soma}")