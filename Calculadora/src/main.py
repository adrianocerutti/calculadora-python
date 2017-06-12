from calculos.funcoes_aritmeticas import somar,subtrair,multiplicar,dividir,porcentagem

print(" ** SEJA BEM VINDO A CALCULADORA PYTHON 1.0 **\n ")
while True:
    print("1. Adição...")
    print("2. Subtração...")
    print("3. Multiplicação...")
    print("4. Divisão...")
    print("5. Porcentagem...")
    print("6. Sair do programa")
    print("\n")

    try:
        opcao = int(input("Selecione qual operação deseja realizar: "))

        if opcao == 1:
            valor1 = float(input("\nDigite o primeiro valor: "))
            valor2 = float(input("Digite o segundo valor: "))
            resultado = somar(valor1,valor2)
            print("\n ** Resultado: {valor1} + {valor2} = {resultado} ** \n".format(valor1=valor1,
                                                                                    valor2=valor2,
                                                                                    resultado=somar(valor1,valor2)))
        elif opcao == 2:
            valor1 = float(input("\nDigite o primeiro valor: "))
            valor2 = float(input("Digite o segundo valor: "))
            resultado = subtrair(valor1, valor2)
            print("\n ** Resultado: {valor1} - {valor2} = {resultado} ** \n".format(valor1=valor1,
                                                                                    valor2=valor2,
                                                                                    resultado=subtrair(valor1, valor2)))
        elif opcao == 3:
            valor1 = float(input("\nDigite o primeiro valor: "))
            valor2 = float(input("Digite o segundo valor: "))
            resultado = multiplicar(valor1, valor2)
            print("\n ** Resultado: {valor1} x {valor2} = {resultado} ** \n".format(valor1=valor1,
                                                                                    valor2=valor2,
                                                                                    resultado=multiplicar(valor1, valor2)))
        elif opcao == 4:
            valor1 = float(input("\nDigite o primeiro valor: "))
            valor2 = float(input("Digite o segundo valor: "))
            try:
                resultado = dividir(valor1, valor2)
                print("\n ** Resultado: {valor1} / {valor2} = {resultado} ** \n".format(valor1=valor1,
                                                                                        valor2=valor2,
                                                                                        resultado=dividir(valor1, valor2)))
            except:
                print("\n ** Erro - Não é possível realizar divisão por zero ** \n")

        elif opcao == 5:
            valor1 = float(input("\nDigite o primeiro valor: "))
            valor2 = float(input("Digite o valor da porcentagem: "))
            resultado = porcentagem(valor1, valor2)
            print("\n ** Resultado: {valor1} + {valor2}% = {resultado} ** \n".format(valor1=valor1,
                                                                                    valor2=valor2,
                                                                                    resultado=porcentagem(valor1, valor2)))
        elif opcao == 6:
            break
        else:
            print("\n Opção inválida! \n")
    except ValueError:
        print("\n ** Erro - Não são permitidas letras ou caracteres especiais ** \n")

print("\n ** Obrigado por usar meu software! ** \n")