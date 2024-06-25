# Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu.
# O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

BONUS = 1000

nome_usuario = input('Informe seu nome: ')
salario_usuario = float(input('Informe seu salario: '))
bonus_usuário = float(input('Informe seu bonus: '))

valor_bonus_calculado = BONUS + salario_usuario * bonus_usuário

print(f'Olá, {nome_usuario}, seu salário com o bonus será de R${valor_bonus_calculado}')

