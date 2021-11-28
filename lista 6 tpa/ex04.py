# Escreva um algoritmo para imprimir na tela a tabuada de um número informado pelo usuário

val = int(input("Digite um numero: "))
for i in range(0,11):
    prod = val * i
    print(f"{val} x {i} = {prod}")