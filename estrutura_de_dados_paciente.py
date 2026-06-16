print("COVID-19")
suspeitos = 0
num_pac = int(input("Informe a quantidade de pacientes:"))
for i in range(num_pac):
    print("=== PACIENTE", i + 1, "===")  # Vai começar a partir do 1.
    tosse = int(input("Você está tossindo? \n1.SIM \n2.NÃO \nResp.:"))
    febre = int(input("Você está com febre? \n1.SIM \n2.NÃO \nResp:"))
    resp = int(input("Você está com dificuldade de respirar? \n1.SIM \n2.NÃO \nResp:"))

    if tosse == 1 and febre == 1 and resp == 1:
        suspeitos += 1 #suspeitos = suspeitos + 1]

print("===================================")
print(f"SUSPEITOS DE COVID-19: {suspeitos}.")
print("===================================")
