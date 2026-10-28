
historico = []

while True:
    valor = float(input("Digite o valor da compra (0 para encerrar): R$ "))

    if valor == 0:
        break

    if valor < 0:
        print("Valor inválido! Digite um valor positivo.")
        continue

    # Solicita novamente a idade enquanto ela for negativa
    while True:
        idade = int(input("Digite a idade do cliente: "))

        if idade < 0:
            print("Idade inválida! Digite uma idade positiva.")
        else:
            break

    valor_original = valor
    desconto_idade = 0
    desconto_valor = 0

    # Desconto de 20% para clientes com 65 anos ou mais
    if idade >= 65:
        desconto_idade = valor * 0.20
        valor -= desconto_idade

    # Desconto adicional de 10% se o valor restante for maior que R$ 100
    if valor > 100:
        desconto_valor = valor * 0.10
        valor -= desconto_valor

    print(f"Valor final: R$ {valor:.2f}")

    compra = {
        "valor_original": valor_original,
        "idade": idade,
        "desconto_idade": desconto_idade,
        "desconto_valor": desconto_valor,
        "valor_final": valor
    }

    historico.append(compra)

# Resumo das compras
print("\n========== RESUMO DO DIA ==========")

total_bruto = 0
total_descontos = 0
total_final = 0

for compra in historico:
    total_bruto += compra["valor_original"]
    total_descontos += (
        compra["desconto_idade"] + compra["desconto_valor"]
    )
    total_final += compra["valor_final"]

print(f"Quantidade de compras: {len(historico)}")
print(f"Total bruto: R$ {total_bruto:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Total final: R$ {total_final:.2f}")
print("===================================")
