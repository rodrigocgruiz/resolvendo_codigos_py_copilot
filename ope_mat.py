#vamos solicitar como estrada dois numeros e depois vamos realizar uma operação matemática

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    result = num1 + num2
elif operacao == "-":
    result = (abs(num1 - num2))
elif operacao == "*":
    result = num1 * num2    
elif operacao == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Divisão por zero não é permitida.")
else:
    print("Operação inválida.")
    result = "Operação inválida."

print("O resultado da operação é:", result)