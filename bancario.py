menu = """

    [d] Depósito
    [s] Sacar
    [e] Extrato
    [q] Quitar
    
   => """
   
saldo = 0
limite = 500
extrato =''
numero_saques = 0
LIMITE_SAQUES = 3   


   
while True:
    
    opcao = input (menu) 
    
    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito:R${valor:.2f}/n"
        else:
            print('Valor inválido')
    
    
    elif opcao == "s":
        valor = float(input("Informe o valor do Saque: "))
         
        excedeu_saldo = valor > saldo 
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques > LIMITE_SAQUES   
        
        if excedeu_saldo:
            print('Saldo insuficiente')
        elif excedeu_limite:
            print('Limite Insuficiente')
        elif excedeu_saques:
            print('Limite de saques excedido')
               
                    
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:R${valor:.2f}/n"
            numero_saques =+ 1   
        else:
            
            print('Valor inválido')    
            
    elif opcao == "e":
        
        print("\n======================== EXTRATO ===================")
        print("NÃO FORAM REALIZADAS OPERAÇÕES" if not extrato else extrato)
        print("==================================================")
        print(f"Saldo: R${saldo:.2f}")
        print("==================================================")      

    elif opcao == "q":
        break
    else:
        print('Informe a operação a ser Realizada')   