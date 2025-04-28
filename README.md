# Sistema-Bancario-Python

## Documentação do Sistema Bancário

### Descrição Geral

O sistema bancário tem como objetivo gerenciar operações bancárias simples, como saques, depósitos e geração de extrato. Ele permite ao usuário realizar saques até um limite diário, depósitos, e acompanhar o extrato detalhado das operações realizadas. Além disso, há controles de saldo e de quantidade de saques realizados por dia, garantindo uma gestão segura e organizada das transações.

### Funções do Sistema

1. **Sacar**: Permite ao usuário realizar saques de sua conta, respeitando o limite de até 500 reais por operação e um limite de 3 saques diários.
2. **Depositar**: Permite ao usuário depositar valores na sua conta, atualizando o saldo.
3. **Gerar Extrato**: Exibe todas as operações realizadas (saques e depósitos) com o respectivo valor e saldo após cada operação. 
4. **Sair**: Encerra o programa.

### Regras e Restrições

1. **Limite de saques por dia**: O sistema permite apenas 3 saques por dia.
2. **Limite de valor para saque**: Cada saque pode ser de no máximo 500 reais.
3. **Exibição de Extrato**: O extrato exibirá o histórico de operações realizadas, com a descrição do tipo da operação (Saque ou Depósito), o valor da operação, e o saldo após cada operação.
4. **Validação de Saque**: O sistema verifica se o valor do saque não ultrapassa o saldo disponível na conta. Se o saque for maior que o saldo, uma mensagem de erro é exibida.
5. **Opções de Menu**: O sistema apresenta um menu com as opções de realizar um saque, depósito, gerar extrato ou sair do programa. 

### Estrutura de Dados

- **Saldo**: Valor atual disponível na conta bancária.
- **Extrato**: Lista que armazena as operações realizadas, incluindo o tipo de operação, valor da operação e saldo final após a operação.
- **Limite de saques**: Define o número máximo de saques permitidos por dia (3).
- **Limite de valor de saque**: Define o valor máximo permitido para cada saque (500 reais).
- **Número de saques**: Contabiliza a quantidade de saques realizados durante o dia.

### Funções Detalhadas

#### 1. **clear()**
   - **Descrição**: Limpa a tela do terminal. Utiliza o comando `cls` para sistemas Windows.
   - **Parâmetros**: Nenhum.
   - **Retorno**: Nenhum.

#### 2. **sacar(saldo_atual, extrato)**
   - **Descrição**: Realiza um saque da conta. Verifica se o valor do saque não ultrapassa o saldo e se o limite de saques do dia não foi atingido.
   - **Parâmetros**: 
     - `saldo_atual`: O saldo atual da conta.
     - `extrato`: Lista que contém o histórico de operações.
   - **Retorno**: O novo saldo após o saque.

#### 3. **depositar(saldo, extrato)**
   - **Descrição**: Realiza um depósito na conta, atualizando o saldo.
   - **Parâmetros**: 
     - `saldo`: O saldo atual da conta.
     - `extrato`: Lista que contém o histórico de operações.
   - **Retorno**: O novo saldo após o depósito.

#### 4. **gerar_extrato(saldo, extrato)**
   - **Descrição**: Exibe o extrato bancário com o histórico de operações realizadas, incluindo tipo de operação, valor e saldo final.
   - **Parâmetros**: 
     - `saldo`: O saldo atual da conta.
     - `extrato`: Lista que contém o histórico de operações.
   - **Retorno**: Nenhum.

### Variáveis do Sistema

- **saldo**: Valor inicial de 1000 reais, que pode ser alterado por saques ou depósitos.
- **extrato**: Lista que armazena todas as operações realizadas (saques e depósitos).
- **qnt_saques_feitos**: Contabiliza a quantidade de saques realizados no dia, com limite de 3 saques por dia.

### Constantes

- **NUM_LIMITE_SAQUES**: Define o número máximo de saques permitidos por dia (3).
- **LIMITE_POR_SAQUE**: Define o valor máximo permitido para cada saque (500 reais).

### Exemplo de Execução

#### Menu de Opções

O sistema apresenta um menu interativo que permite ao usuário selecionar entre as opções de **Sacar**, **Depositar**, **Gerar Extrato** ou **Sair**:

```plaintext
========= Sistema Bancário Edus ==========
[1] - Sacar
[2] - Depositar
[3] - Gerar Extrato
[0] - Sair

Selecione uma das opções
===========================================
>
```

### Fluxo de Operações

1. **Saque**: O usuário escolhe a opção de saque, insere o valor desejado, e o sistema verifica se o valor é válido (não maior que o saldo disponível e respeitando o limite de 500 reais por operação).
2. **Depósito**: O usuário escolhe a opção de depósito, insere o valor desejado, e o sistema atualiza o saldo com o valor depositado.
3. **Extrato**: O usuário escolhe a opção de gerar o extrato. O sistema exibe o histórico de operações realizadas, com valores formatados em reais.
4. **Sair**: O usuário escolhe a opção de sair, encerrando o sistema.

### Exemplos de Mensagens

- **Erro de Saque**: "O valor inválido, tente outro valor."
- **Saque Realizado com Sucesso**: "Saque no valor de 200,00 reais realizado com sucesso, novo saldo é de 800,00 reais."
- **Limite de Saques**: "O limite de Saques do dia já foi alcançado, tente novamente amanhã."
- **Extrato**: Exibe todas as operações realizadas, com o tipo da operação, valor e saldo final.
