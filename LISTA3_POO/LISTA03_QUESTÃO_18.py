equipamentos = []

for i in range(1, 6):
    print(f"\n--- Equipamento {i} ---")
    nome = input("Nome do equipamento: ")
    preco = float(input("Preco (R$): "))
    equipamentos.append({"nome": nome, "preco": preco})

print("\n=== EQUIPAMENTOS CADASTRADOS ===")
for eq in equipamentos:
    print(f"- {eq['nome']}: R$ {eq['preco']:.2f}")

mais_caro = max(equipamentos, key=lambda x: x["preco"])

print(f"\nEquipamento mais caro: {mais_caro['nome']} (R$ {mais_caro['preco']:.2f})")