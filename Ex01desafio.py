contador = ('zero', 'um', 'dois', 'tres', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'catorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito',
            'dezenove', 'vinte')

while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <=20: #validação para confirmar se o número esta entre 0 e 20
        print(f'Você digitou o número {contador[numero]}')
    else:
        print("Numero errado")
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if continuar == "N":
        break
    while continuar != "N" and continuar !="S":
        continuar=str(input("Deseja continuar? [S/N] ")).upper().strip()[0]