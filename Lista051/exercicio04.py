'''
Desenvolver um programa que apresente o valor da soma dos cem primeiros números inteiros (1 + 2 + 3 + 4 + ...
+ 97 + 98 + 99 + 100)
'''

# Contadores

cont = 1
acumulador = 0

# Laços e Prints

while cont <= 100:
    acumulador = acumulador + cont
    cont = cont + 1
print(f"A soma dos valores de 1 a 100 = {acumulador}")