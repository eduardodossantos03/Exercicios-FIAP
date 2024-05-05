
valor_do_carro = float(input('Por favor, insira o valor do carro que deseja comprar: '))


compra_a_vista = valor_do_carro * (20 / 100)
valor_final = valor_do_carro - compra_a_vista
print(f'O preço final á vista com 20% de desconto é: R$ {valor_final}')


for i in range(6, 61, 6): 
    parcelas = valor_do_carro * (i/ 2) /100 
    valor_parcelado = parcelas + valor_do_carro
    valor_da_parcelas = valor_parcelado / i
    print(f'preço final parcelado em {i}x é R${valor_parcelado} com parcelas de R$ {valor_da_parcelas:.2f}')