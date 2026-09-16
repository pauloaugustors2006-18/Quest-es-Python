adequados = 0
lentos = 0
soma_latencias = 0
maior_latencia = 0

for i in range(1, 11):
    latencia = float(input(f"Digite a latencia do teste {i} (ms): "))
    soma_latencias += latencia
    
    if latencia <= 100:
        adequados += 1
    else:
        lentos += 1
        
    if i == 1 or latencia > maior_latencia:
        maior_latencia = latencia

media = soma_latencias / 10

print("\n--- Relatorio Final da Rede ---")
print(f"Testes adequados (<= 100 ms): {adequados}")
print(f"Testes com lentidao (> 100 ms): {lentos}")
print(f"Media das latências: {media:.2f} ms")
print(f"Maior latencia registrada: {maior_latencia} ms")