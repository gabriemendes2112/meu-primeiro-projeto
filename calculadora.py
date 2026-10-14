
print("=== CALCULADORA ===")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = input("Escolha uma opção: ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == "1":
    print("Resultado:", num1 + num2)
elif opcao == "2":
    print("Resultado:", num1 - num2)
elif opcao == "3":
    print("Resultado:", num1 * num2)
elif opcao == "4":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Não é possível dividir por zero!")
else:
    print("Opção inválida!")
