# PROGRAMA PARA CALCULAR NOTA E DECIDIR APROVADO OU REPROVADO

#ETAPA 2 - ESTRUTURA SEQUENCIAL

# Início do programa com nome que definimos (cabeçalho).
print("=== HISTORIX ===")

print("Notas da matéria de MATEMÁTICA")

# --- Coleta de dados ---

# Pede nome do aluno.
nome = input("Nome do aluno: ")

# Pede frequência do aluno.
frequencia = float(input("Frequência do aluno (%): "))

# Pede nota da prova (float).
# Esperado: 0 a 5.
prova = float(input("Nota da prova (0 a 5): "))

# Pede nota do teste (float).
# Esperado: 0 a 3.
teste = float(input("Nota do teste (0 a 3): "))

# Pede nota do caderno (float).
# Esperado: 0 a 2.
caderno = float(input("Nota do caderno (0 a 2): "))

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

# Primeiro verifica frequência
if frequencia < 75:
    print("Situação(Frequência): REPROVADO POR FREQUÊNCIA")
else:
    print("Situação(Frequência): APROVADO POR FREQUÊNCIA")

# --- Resultado final do bimestre ---

# Se reprovar por nota OU frequência
if nota_final < 5 or frequencia < 75:
    print("Você está REPROVADO neste bimestre.")

# Se passar nos dois critérios
else:
    print("Parabéns! Você está APROVADO neste bimestre.")
