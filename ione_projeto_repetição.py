# PROGRAMA PARA CALCULAR NOTAS DE MÚLTIPLAS DISCIPLINAS

print("=== HISTORIX ===")

# Pede nome do aluno
nome = input("Nome do aluno: ")

# Quantidade de disciplinas
quantidade = int(input("Quantas disciplinas deseja cadastrar? "))

# Repetição para várias disciplinas
for i in range(quantidade):

    print("\n=== DISCIPLINA", i + 1, "===")

    # Nome da disciplina
    disciplina = input("Nome da disciplina: ")

    # Frequência
    frequencia = float(input("Frequência do aluno (%): "))

    # Validar frequência
    while frequencia < 0 or frequencia > 100:
        print("Digite uma frequência válida entre 0 e 100.")
        frequencia = float(input("Frequência do aluno (%): "))

    # Nota da prova
    prova = float(input("Nota da prova (0 a 5): "))

    # Validar prova
    while prova < 0 or prova > 5:
        print("Digite uma nota válida entre 0 e 5.")
        prova = float(input("Nota da prova (0 a 5): "))

    # Nota do teste
    teste = float(input("Nota do teste (0 a 3): "))

    # Validar teste
    while teste < 0 or teste > 3:
        print("Digite uma nota válida entre 0 e 3.")
        teste = float(input("Nota do teste (0 a 3): "))

    # Nota do caderno
    caderno = float(input("Nota do caderno (0 a 2): "))

    # Validar caderno
    while caderno < 0 or caderno > 2:
        print("Digite uma nota válida entre 0 e 2.")
        caderno = float(input("Nota do caderno (0 a 2): "))

    # Cálculo da nota final
    nota_final = prova + teste + caderno

    # Resultado
    print("\n=== RESULTADO ===")
    print("Aluno:", nome)
    print("Disciplina:", disciplina)
    print("Nota final:", nota_final)

    # Situação pela nota
    if nota_final == 10:
        print("Situação(notas): EXCELENTE")

    elif nota_final >= 5:
        print("Situação(notas): APROVADO")

    else:
        print("Situação(notas): REPROVADO")

    # Situação pela frequência
    if frequencia < 75:
        print("Situação(Frequência): REPROVADO POR FREQUÊNCIA")

    else:
        print("Situação(Frequência): APROVADO POR FREQUÊNCIA")

    # Resultado final do bimestre

    # Se reprovar por nota
    if nota_final < 5:
        print("Você está REPROVADO neste bimestre.")

    # Se passar na nota mas reprovar por frequência
    elif nota_final >= 5 and frequencia < 75:
        print("Você está de RECUPERAÇÃO, consultar professor.")

    # Se passar nos dois critérios
    else:
        print("Parabéns! Você está APROVADO neste bimestre.")


