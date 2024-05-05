op = -1

while op != 1:
    print('Por favor selecione a plataforma de investimento que deseja resgatar seu investimento: ')
    print("1 - CDB (Certificado de Depósito Bancário)")
    print("2 - LCI (Letra de Crédito Imobiliário)")
    print("3 - LCD (Letra de Crédito do Agronegócio)")

    op = int(input("Informe sua opção: "))
    op2 = int(input('Informe o valor a ser resgatado: '))
    op3 = int(input('Informe quantos dias o seu dinheiro ficou investido: '))

    if op == 1:
        if op3 <= 180:
            x = op2 * 0.225
            print(f'O valor do seu IR será de: {x}')
        elif 180 < op3 <= 360:
            y = op2 * 0.20
            print(f'O valor do seu IR será de: {y}')
        elif 360 < op3 <= 720:
            e = op2 * 0.175
            print(f'O valor do seu IR será de: {e}')
        elif op3 > 720:
            j = op2 * 0.15
            print(f'O valor do seu IR será de: {j}')
    else:
        print(' voce não possui um IR.')

