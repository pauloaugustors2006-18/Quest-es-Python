identificadores = [id_num for id_num in range(1, 20) if id_num % 2 == 0]

media = sum(identificadores) / len(identificadores)

print(f"Identificadores considerados: {identificadores}")
print(f"Média dos identificadores: {media:.2f}")