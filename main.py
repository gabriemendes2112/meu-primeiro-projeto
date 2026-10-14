
gastos = []

while True:
    print("=== CONTROLE DE GASTOS ===")
    print("1 - Cadastrar gasto")
    print("2 - Listar gastos")
    print("3 - Ver total gasto")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do gasto: ")
        valor = float(input("Digite o valor do gasto: "))

        gastos.append([nome, valor])

        print("Gasto cadastrado!")
        print(f"Descrição: {nome}")
        print(f"Valor: R$ {valor:.2f}")

    elif opcao == "2":
        print("=== SEUS GASTOS ===")

        for gasto in gastos:
            print(f"{gasto[0]} - R$ {gasto[1]:.2f}")

    elif opcao == "3":
        total = 0

        for gasto in gastos:
            total = total + gasto[1]

        print(f"Total gasto: R$ {total:.2f}")

    elif opcao == "4":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida!")
