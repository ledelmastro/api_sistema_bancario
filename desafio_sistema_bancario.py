menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[a] Ajustar Limite
[p] Pix
[q] Sair

=> """

import re
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
novo_limite = 0
saldo_destino = 0
extrato_destino = 0

while True:
    opcao = (input(menu))

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "a":
        valor = float(input("Informe o valor do novo limite: "))
        if valor > 0 and valor < 500:
            limite = valor
            extrato += f"Novo limite: R$ {limite:.2f}\n"            
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "p":
        chave_pix = str(input("Informe a chave Pix do destinatário, no formato (xx)9999-9999 ou CPF/CNPJ separado por pontos e barras: "))
        padrao_tel = r'\(\d{2}\)9\d{4}-\d{4}'
        padrao_cpf = "^\d{3}\.\d{3}\.\d{3}\-\d{2}$"
        padrao_cnpj = "^\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}$"
        
        if re.match(padrao_tel, chave_pix) or re.match(padrao_cnpj, chave_pix) or re.match(padrao_cpf, chave_pix):
            valor = float(input("Informe o valor do Pix: "))
            if valor > 0:
                saldo += valor
                extrato += f"Novo Pix: R$ {saldo:.2f}\n"
    #   except:
        else:
            print ("Operação falhou! O valor informado é inválido. Informe a chave Pix do destinatário no formato (xx)9999-9999 ou CPF/CNPJ separado por pontos e barras.")    

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
