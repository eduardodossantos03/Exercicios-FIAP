def calculo_de_parcelas(debito):
    taxa  = {
        1: 0,
        3: 10,
        6: 15,
        9: 20,
        12: 25
    }

    print(f"{'Valor da dívida':<15} {'Juros':<10} {'Número de parcelas':<20} {'Valor da parcela':<20}")

    for parcelas, taxa  in taxa.items():
        valores = debito * (taxa / 100)
        total_debito = debito + valores 
        valores_da_parcela = total_debito / parcelas
        print("R$ {:<13,.2f} R$ {:<8,.2f} {:<18} R$ {:<18,.2f}".format(total_debito, valores , parcelas, valores_da_parcela))

debito = float(input("Digite o valor da dívida: "))
calculo_de_parcelas(debito)