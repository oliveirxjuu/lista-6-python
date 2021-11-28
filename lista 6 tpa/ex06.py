# Escreva um algoritmo que receba um número e imprima na tela do zero até o número digitado pelo usuário.

razao = int(input("Digite a razão: "))
a = int(input("Digite o numero que será multiplicado: "))

cont = 1

while cont <= 5 :
    a = razao * a
    cont = cont + 1
    print (a)