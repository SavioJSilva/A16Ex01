print('Números por extenso de 0 a 20')
print('')
while True:
    numero = int(input('Digite um número: '))
    while numero > 20:
        print('Digito incorreto! Digite novamente:')
        numero = int(input('Digite um número: '))
    num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
           'Dezenove', 'Vinte')
    for nn, n in enumerate(num):
        if numero == nn:
            print(f'Você digitou o número {n}.')
    cont = str(input('Quer continuar mostrando números por extenso? [S/N] ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('Quer continuar mostrando números por extenso? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print('#' * 60)