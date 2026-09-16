while True:
    print("\n=== CONVERSOR DE TEMPERATURAS ===")
    temp = float(input("Digite o valor da temperatura: "))
    
    print("\nEscolha a conversão:")
    print("1 - Celsius para Fahrenheit")
    print("2 - Celsius para Kelvin")
    print("3 - Fahrenheit para Celsius")
    print("4 - Kelvin para Celsius")
    opcao = input("Opcao desejada (1-4): ")

    if opcao == '1':
        res = (temp * 9/5) + 32
        print(f"\n{temp}°C equivale a {res:.2f}°F")
    elif opcao == '2':
        res = temp + 273.15
        print(f"\n{temp}°C equivale a {res:.2f}K")
    elif opcao == '3':
        res = (temp - 32) * 5/9
        print(f"\n{temp}°F equivale a {res:.2f}°C")
    elif opcao == '4':
        res = temp - 273.15
        print(f"\n{temp}K equivale a {res:.2f}°C")
    else:
        print("\nOpçao invalida! Tente novamente.")
        continue

    deseja_continuar = input("\nDeseja realizar outra conversão? (s/n): ").strip().lower()
    if deseja_continuar != 's':
        print("\nPrograma encerrado. Até mais!")
        break