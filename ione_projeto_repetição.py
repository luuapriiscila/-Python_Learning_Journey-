# PROGRAMA PARA CALCULAR NOTAS DE MÚLTIPLAS DISCIPLINAS

#ETAPA 4 - ESTRUTURA DE REPETIÇÃO 

# Início do programa com nome que definimos (cabeçalho).
print("=== HISTORIX ===")

# Pede nome do aluno.
nome = input("Nome do aluno: ")

# Quantidade de disciplinas
quantidade = int(input("Quantas disciplinas deseja cadastrar? "))

# Repetição para múltiplas disciplinas
for i in range(quantidade):

    print("=== DISCIPLINA", i + 1, "===")#Vai começar a partir do 1.

    # Nome da disciplina
    disciplina = input("Nome da disciplina: ")

    # Pede nota da prova
    prova = float(input("Nota da prova (0 a 5): "))

    # Validar nota da prova
    while prova < 0 or prova > 5:
        print("Digite uma nota válida entre 0 e 5.")
        prova = float(input("Nota da prova (0 a 5): "))

    # Pede nota do teste
    teste = float(input("Nota do teste (0 a 3): "))

    # Validar nota do teste
    while teste < 0 or teste > 3:
        print("Digite uma nota válida entre 0 e 3.")
        teste = float(input("Nota do teste (0 a 3): "))

    # Pede nota do caderno
    caderno = float(input("Nota do caderno (0 a 2): "))

    # Validar nota do caderno
    while caderno < 0 or caderno > 2:
        print("Digite uma nota válida entre 0 e 2.")
        caderno = float(input("Nota do caderno (0 a 2): "))

    # Quantidade de faltas do aluno
    faltas = int(input("Quantidade de faltas: "))

    # Validar faltas
    while faltas < 0:
        print("Digite uma quantidade válida de faltas.")
        faltas = int(input("Quantidade de faltas: "))

    # Total de aulas
    total_aulas = 200

    # Limite de faltas permitido (25%)
    limite_faltas = total_aulas * 0.25

    # --- Cálculo da nota ---

    # Soma todas as notas.
    nota_final = prova + teste + caderno

    # --- Exibição de resultados ---

    print("=== RESULTADO ===")

    # Exibe nome do aluno.
    print("Aluno:", nome)

    # Exibe disciplina
    print("Disciplina:", disciplina)

    # Exibe nota final.
    print("Nota final:", nota_final)

    # Exibe faltas
    print("Faltas:", faltas)
    

    # --- Lógica de situação ---

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



