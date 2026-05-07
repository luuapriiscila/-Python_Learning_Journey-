# PROGRAMA PARA CALCULAR NOTA E DECIDIR APROVADO OU REPROVADO

#ETAPA 3 - ESTRUTURA DE DECISÃO

# Início do programa com nome que definimos (cabeçalho).
print("=== HISTORIX ===")

print("Notas da matéria de MATEMÁTICA")

# --- Coleta de dados ---

# Pede nome do aluno.
nome = input("Nome do aluno: ")

# Pede nota da prova (float).
# Esperado: 0 a 5.
prova = float(input("Nota da prova (0 a 5): "))

# Pede nota do teste (float).
# Esperado: 0 a 3.
teste = float(input("Nota do teste (0 a 3): "))

# Pede nota do caderno (float).
# Esperado: 0 a 2.
caderno = float(input("Nota do caderno (0 a 2): "))

# Quantidade de faltas do aluno
faltas = int(input("Quantidade de faltas: "))

# Total de aulas
total_aulas = 200

# Limite de faltas permitido (25%)
limite_faltas = total_aulas * 0.25

# --- Cálculo da nota ---

# Soma todas as notas.
nota_final = prova + teste + caderno

# --- Exibição de resultados ---

# Formatação e cabeçalho.
print("=== RESULTADO ===")

# Exibe nome do aluno.
print("Aluno:", nome)

# Exibe nota final.
print("Nota final:", nota_final)

# Exibe faltas
print("Faltas:", faltas)

#ETAPA 3 ESTRUTURA DE DECISÃO

# --- Lógica de situação ---

# Avalia situação do aluno.

# Nota >= 10: EXCELENTE.
if nota_final == 10:

  print("Situação(notas): EXCELENTE")

# Senão, nota >= 5: APROVADO.
elif nota_final >= 5:

  print("Situação(notas): APROVADO")

# Senão: REPROVADO.
else:

  print("Situação(notas): REPROVADO")

# --- Lógica de frequência ---

# Primeiro verifica frequência pelas faltas
if faltas > limite_faltas:
    print("Situação(Frequência): REPROVADO POR FALTA")

else:
    print("Situação(Frequência): APROVADO POR FREQUÊNCIA")

# --- Resultado final do bimestre ---

# Se reprovar na nota e na frequência
if nota_final < 5 and faltas > limite_faltas:
    print("Situação(final): Você está REPROVADO neste bimestre.")

# Se reprovar apenas em um dos critérios
elif nota_final < 5 or faltas > limite_faltas:
    print("Situação(final): RECUPERAÇÃO, consulte um professor.")

# Se passar nos dois critérios
else:
    print("Situação(final): Parabéns! Você está APROVADO neste bimestre.")
