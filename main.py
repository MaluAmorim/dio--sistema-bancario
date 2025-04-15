import time

# Definindo o valor das variáveis e constantes
saldo = 1000.0
depositos_realizados = 0
valor_dos_depositos = []
saques_realizados = 0
valor_dos_saques = []
LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500.0

print("Abrindo o LumosBank...", end="\r")
time.sleep(3)

print("Bem vindo ao LumosBank! \n")

opcao = 0

# Loop que mantem o sistema funcionando até que seja escolhida a opção 4 para sair
while opcao != 4:
    print("As opções são: \n[1] Depositar \n[2] Sacar \n[3] Extrato \n[4] Sair \n")
    
    try:
        opcao = int(input("Digite a opção desejada: ")) # Recebe a opção escolhida pelo usuário
        # Ao ser escolhida a opção 1 é feito o tratamento de deposito na conta
        if opcao == 1:
            try:
                deposito = float(input("Digite a quantia a ser depositada: ")) # Recebe o valor a ser depositado
                
                if deposito > 0: # Caso seja um número positivo da continuidade ao código
                        saldo += deposito
                        depositos_realizados += 1
                        valor_dos_depositos += [deposito]
                        print("Depósito realizado! \n")

                else: # Caso o valor informado seja invalido é informado ao usuário e solicitado novamente a inserção
                    print("O valor deve ser positivo.\n")
                    time.sleep(3)

            except ValueError: # Trata erro ao ser inserido um valor string
                    print("Entrada inválida. Por favor, digite um número válido. Não utilize vigulas mas sim ponto. Ex.: 275.49\n")

        # Ao ser escolhida a opção 2 é feito o tratamento de saque
        elif opcao == 2:
            if saques_realizados >= LIMITE_SAQUES: # Caso a quantidade de saques seja maior ou iqual ao limete de saques o mesmo será impedido
                print("Limite de saques diários atingido.\n")
            
            # Da continuidade ao saque
            else:
                try:
                    saque = float(input("Digite o quantia a ser retirada: ")) # Recebe o valor a ser retirado da conta

                    if saque > LIMITE_VALOR_SAQUE: # Caso o valor enserido seja maior do que o limite é informado e solcitado que insira novamente
                        print(f"O valor máximo para saque é R${LIMITE_VALOR_SAQUE:.2f}.\n")

                    elif saque > saldo: # Se o valor para saque for maior do que o valor em conta o usuário terá que digitar novamente
                        print(f"Saldo insuficiente! Saldo disponível: {saldo:.2f} \n")

                    elif saque <= 0: # Informa que o valor tem q ser positivo fazendo o usuário digitar novamente
                        print("O valor deve ser positivo.\n")

                    else: # Código continua normalmente
                        saldo -= saque
                        saques_realizados += 1
                        valor_dos_saques += [saque]
                        print("Saque realizado!\n")
                
                except ValueError: # Trata erro ao ser inserido um valor string
                    print("Entrada inválida. Por favor, digite um número válido. Não utilize vigulas mas sim ponto. Ex.: 275.49\n")

        elif opcao == 3: # Responsavel por mostrar o extrato da conta
            print("==========Extrato==========")
            if valor_dos_depositos:
                print("Depósitos realizados: \n")

                for i, valor in enumerate(valor_dos_depositos, start=1): # Mostra o valor de todos os depósitos realizados
                    print(f"  {i}. R${valor:.2f} \n")

            else:
                print("Nenhum depósito realizado. \n")

            if valor_dos_saques:
                print("Saques realizados: \n")
                print(f"Saques realizados hoje: {saques_realizados} de {LIMITE_SAQUES}\n") # Informa quantos saques ja foram realizados e qual o limite diário
                
                for i, valor in enumerate(valor_dos_saques, start=1): # Mostra o valor de todos os saques realizados
                    print(f"  {i}. R${valor:.2f} \n")

            else:
                print("Nenhum saque realizado. \n")

            
            print(f"O saldo atual é de R${saldo:.2f}\n") # Mostra o saldo atual
            print("===========================")
            time.sleep(3)

        elif opcao == 4: # Encerra o programa
            print("Agradecemos a preferência, até breve!")
        
        else:
            print("Opção inválida. Tente novamente.\n")

    except ValueError: # Trata erro ao ser inserido um valor string
                    print("Entrada inválida. Digite somente números. \n")
