num = ('zero', 'um', 'dois', 'tres', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'catorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito',
            'dezenove', 'vinte')
while True:
    resposta=int(input("Digite um número entre 0 e 20: "))
    if 0 <= resposta <=20:
        print("Você digitou {}" .format(num[resposta]))
        resposta=str(input("Deseja continuar?[S/N ")).upper().strip()[0]
        if resposta == "N":
            break
        while resposta!="N" and resposta!="S":
            resposta=str(input("Deseja continuar?[S/N] ")).upper().strip()[0]