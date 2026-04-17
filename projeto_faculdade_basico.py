# | MÉDIA SIMPLES DA DISCIPLINA DE MATEMÁTICA

#Pedir a nota do aluno 
aluno_1 = input("Informe o seu NOME COMPLETO:")

# |FORMAS DE AVALIAÇÃO

#Pedir a nota da avaliação
mat_avaliacao = float(input("Informe sua NOTA na AVALIAÇÃO DE MATEMÁTICA(5 pontos):"))
#Se o usuário não colocar de 0 a 5
while mat_avaliacao < 0 or mat_avaliacao > 5:
    print("Informe um valor entre 0 e 5")
    mat_avaliacao = float(input("Informe sua NOTA na AVALIAÇÃO DE MATEMÁTICA (0 a 5): "))
    
#Pedir a nota do teste
mat_teste = float(input("Informe sua NOTA no TESTE DE MATEMÁTICA(3 pontos):"))
#Se o usuário não colocar de 0 a 3
while mat_teste < 0 or mat_teste > 3:
    print("Informe um valor entre 0 e 3")
    mat_teste = float(input("Informe sua NOTA no TESTE DE MATEMÁTICA (0 a 3): "))
    
#Pedir a nota do caderno
#Se o usuário não colocar de 0 a 2
mat_caderno = float(input("Informe sua NOTA no VISTO DE CADERNO DE MATEMÁTICA(2 pontos):"))
while mat_caderno < 0 or mat_caderno > 2:
    print("Informe um valor entre 0 e 2")
    mat_caderno = float(input("Informe sua NOTA no VISTO DE CADERNO DE MATEMÁTICA (0 a 2): "))

#Cálculo da Média 
media = mat_avaliacao + mat_teste + mat_caderno 

print("Aluno(a)", aluno_1 ,".Sua média em MATEMÁTICA é:" , media)
