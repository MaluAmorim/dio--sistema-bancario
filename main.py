import time

saldo = 1500.0

print("Abrindo o LumosBank...", end="\r")
time.sleep(3)

print("Bem vindo ao LumosBank! \n")

opcao = 0

while opcao != 4:
    print("As opções são: \n[1] Depositar \n[2] Sacar \n[3] Extrato \n[4] Sair \n")

    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        deposito = float(input("Digite a quantia a ser depositada: "))
        saldo += deposito
        print("Deposito realizado! \n")
        time.sleep(3)

    elif opcao == 2:
        saque = float(input("Digite o quantia a ser retirada: "))

        if saldo >= saque:
            saldo -= saque
            print("Saque realizado! \n")
            time.sleep(3)
        
        else:
            print("Saldo insuficiente! \n")

    elif opcao == 3:
        print(f"O saldo atual é de {saldo} \n")
        time.sleep(3)

    else:
        print("Agradecemos a preferência, até breve!")
