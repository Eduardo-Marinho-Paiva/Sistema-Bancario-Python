# Funções do sistema: 
# 1) Sacar 
# 2) Depositar 
# 3) Pegar extrato 
# 4) Sair

# Especificações: 
# 1) Só pode ser feito 3 saques por dia
# 2) Se o saque tiver um valor maior que o saldo, deve aparecer um erro.
# 3) Deve ter um menu 
# 4) O Extrato deve conter todas as operações realizadas, no estilo "Tipo operação : Valor da operação" com o valor formatado em reais e o saldo restante deve aparecer no final de tudo, bem como o saldo inicial antes de listar tudo.
# 5) Cada SAQUE só pode ter até 500 reais



# Bibliotecas 
import os # Para limpar Terminal
import time # Para Pausar tempo do terminal.

# Funções 
def clear():
    os.system("cls") # Para Windows.
    
def sacar(saldo_atual,extrato):
    # Menu
    menu_saldo = f'''
        ======== MENU SAQUE ======== 
        Conta: XXXXX-X
        Saldo da conta: R${saldo_atual:.2f}
        ----------------------------
        Digite quanto deseja sacar:
        >'''
    # Captar valor de saque valido  
    while True:
        valor_saque = float(input(menu_saldo))
        if(saldo_atual >= valor_saque): 
            break
        else:
            print("O valor inválido, tente outro valor.")
            
    if(valor_saque <= 0):
        print("valor de saque não pode ser negativo")
        return saldo_atual
    # Controle de Extrato e confirmação de operação
    novo_saldo = saldo_atual-valor_saque
    print(f"Saque no valor de {valor_saque:.2f} reais realizado com sucesso, novo saldo é de {novo_saldo:.2f} reais")
    extrato.append({"Tipo":"Saque","Valor":valor_saque,"Saldo":novo_saldo})
    return novo_saldo
    
def depositar(saldo,extrato):
    menu = f'''======== MENU DEPÓSITO ======== 
        Conta: XXXXX-X
        Saldo da conta: R${saldo:.2f}
        ----------------------------
        Digite quanto deseja depositar:
        >'''
    valor_deposito = float(input(menu))
    
    if(valor_deposito<=0):
        print("valor de deposito não pode ser negativo !!")
        return saldo
    
    novo_saldo = saldo + valor_deposito
    print(f"Depósito no valor de {valor_deposito:.2f} reais realizado com sucesso, seu novo saldo é de {novo_saldo:.2f} reais")
    extrato.append({"Tipo":"Depósito","Valor":valor_deposito,"Saldo":novo_saldo})
    
    return novo_saldo
        
def gerar_extrato(saldo,extrato):
    x = 1
    print("============ EXTRATO BANCÁRIO ============")
    for operacao in extrato:
        print(f'''
        Operação {x} -----------------------------
        Tipo de Operação: {operacao["Tipo"]}
        Valor da Operação: {operacao["Valor"]} Reais
        Novo Saldo pós operação: {operacao["Saldo"]} Reais
        ------------------------------------------''')
        x+=1
    print(f"O saldo final é de {saldo:.2f} reais ")
    print("Para sair digite 0")
    while True:
        opc = int(input(">"))
        if(opc == 0):
            break
    
        
    

# Variaveis
saldo = 0 
extrato = []
qnt_saques_feitos = 0


# Constantes
NUM_LIMITE_SAQUES = 3
LIMITE_POR_SAQUE = 500



# Inicio do programa

funcoes_sistema = [sacar,depositar,gerar_extrato]

while True: 
    clear()
    menu = '''
        ========== Sistema Bancário Edus ==========
        [1] - Sacar
        [2] - Depositar
        [3] - Gerar Extrato
        [0] - Sair
        
        Selecione uma das opções
        ===========================================
        >'''
    opc = int(input(menu))
    print(opc)
    
    if(opc < 0 or opc > 3): #OPÇÃO INVÁLIDA
        print("Opção Inválida, por favor tente novamente")
        time.sleep(2)
        
        
    elif(opc == 1): # SAQUE
        if(qnt_saques_feitos < 3):
            saldo = sacar(saldo,extrato)
            qnt_saques_feitos+=1
        else: 
            print("O limite de Saques do dia já foi alcançado, tente novamente amanhã")
        time.sleep(2)
        
            
    elif(opc == 2):# DEPOSITO
        saldo = depositar(saldo,extrato)
        time.sleep(2)
        
    elif(opc == 3): # EXTRATO
        if(qnt_saques_feitos <= 0):
            print("O extrato está vazio, realize alguma operação para que esta possa aparecer no extrato")
            time.sleep(2)
            
        else:
            gerar_extrato(saldo,extrato)
    else: 
        clear()
        print("Nós do Banco EDUS o desejamos um ótimo dia, e até a próxima !")
        break
    
