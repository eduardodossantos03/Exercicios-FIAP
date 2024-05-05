num_colaboradores = int(input('Por favor informe a quantidade de colaboradores que irão participar da votação: '))

votos = { '1': 0, '2': 0, '3': 0, '4': 0, '5': 0 }

for _ in range(num_colaboradores):
    print('1. Segunda-Feira')
    print('2. Terça-Feira') 
    print('3. Quarta-Feira')
    print('4. Quinta-Feira')     
    print('5. Sexta-Feira') 

    dia = input("Por favor, informe o dia da semana que tenha mais disponibilidade para ver as lives: ")
    
    if dia in votos:
        votos[dia] += 1
    else:
        print('Resposta incorreta, Por favor tente novamente')

dia_mais_votado = max(votos, key=votos.get)

print(f'O dia mais votado para as lives é o dia {dia_mais_votado}, com um total de {votos[dia_mais_votado]} votos.')