contador = ('zero', 'um', 'dois', 'tres', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'catorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito',
            'dezenove', 'vinte')

while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0<= numero <=20: #validação para confirmar se o número esta entre 0 e 20
        break
    print('O número precisa ser entre 0 e 20. ', end='')  # end='(vazio)' para não pular a linha na resposta
print(f'Você digitou o número {contador[numero]}')



