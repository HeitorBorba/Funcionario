
nome = input('Digite seu nome: ')
ganho_por_hora = float(input('Digite quanto que voce ganha por hora: '))
hrs_trabalhadas = float(input('Digite quantas horas você trabalha por dia: '))
print()


salario_total = ganho_por_hora * hrs_trabalhadas * 20

print(nome + ', se você trabalhar ' + str(hrs_trabalhadas) + ' hrs por dia e ganhar R$ ' + str(ganho_por_hora) + ' por hora , no final do mes tera um salario de ' + str(salario_total) )