'''
Desenvolver um programa que apresente todos os valores numéricos inteiros ímpares situados na faixa de 0 a
20. Para saber se o número é ímpar, será necessário verificar essa condição com o comando if. Sendo ímpar,
mostre-o; não sendo, passe para o próximo passo.
'''

# Contadores

cont = 0

#Laços, Condições e Prints

while cont <= 20:
    resto = cont % 2
    if resto == 1:
        print(f"{cont} é impar")
    cont = cont + 1