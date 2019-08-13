dicionario_de_dias = {
    1: 'Domingo',
    2: 'Segunda-feira',
    3: 'Terça-Feira',
    4: 'Quarta-Feira',
    5: 'Quinta-Feira',
    6: 'Sexta-Feira',
    7: 'Sabado'
}

dia = int(input('Digite um numero de 1 a 7 : '))

try:
    print(dicionario_de_dias[dia])

except:
    print('OPS')