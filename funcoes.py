#Função Cabeçalho
def cabecalho():
    #cabecalho
    print('*'*40)
    print('************FACULDADE CESUSC***********')
    print('CURSO: ANÁLISE E DESENVOLVIMENTO DE SISTEMAS')
    print('Discipl.: LÓGICA DE PROG E ALGORÍTMOS')
    print('Prof. Roberto Fabiano Fernandes')
    print('Turma: ADS: 11 / Ano: 2024')
    print('Avaliação: N2/N3')
    print('*'*40)
    

#Função Menu
def menu():
    #menu
    while True:
        print('Escolha a opção:')
        print('1 - Cadastrar Dados')
        print('2 - Listar Dados')
        print('3 - Alterar Dados')
        print('4 - Excluir Dados')
        print('5 - Realizar Backup do arquivo')
        print('0 - Sair')
        opcao= input('Digite uma opção:')
    
    if opcao== '1':
        cadastrar_dados()
    if opcao== '2':
        listar_dados()
    if opcao== '3':
        alterar_dados
    if opcao== '4':
        excluir_dados
    if opcao== '5':
        realizar_backup
    if opcao== '0':
        break

    
    else:
        print('Opção inválida, digite um número conforme as oções mencioandas')


#Função Cadastrar
def cadastrar():
try:
    #Abrir o arquivo 'Dados.txt' em modo de apêndice (adicionar dados ao final do arquivo)
    with open('Dados.txt', 'a') as arquivo:
        #Solicitar ao usuário as informações do aluno
        nome = input(''))    
        idade
        #Formatar os dados do aluno em uma string
        aluno = f'{nome},{idade}\n'
        #Escrever a string formatada no arquivo 'Dados.txt'
        arquivo.write(aluno)
        #Exibir uma mensagem de sucesso
        print('Dados do alno cadastrados com sucesso!')
except ValueError:
    #Capturar um erro caso os valores fornecidos pelo usuário não estejam no formato esperado
    print('Valor inválido. Verifique as informações e tente novamente')
except Exception as e:
    #Capturar qualquer outro erro que possa ocorrer durante o cadastro dos dados
    print('Ocorreu um erro ao cadastrar os dados:', str(e))


#Função Listar
def listar_dados():
try:
    #Abrir o arquivo 'Dados.txt' em modo de leitura ('r')
    with open('Dados.txt', 'r') as arquivo:
        #Ler todas as linhas do arquivo e armazená-las em uma lista
        linhas = arquivo.readlines()
    #Verificar se não há linhas (dados) no arquivo
    if not linhas:
        print('Nenhum dado de aluno cadastrado,')
    else:
        #Exibir os dados do aluno na tela
        print('Nome: ', nome)
        print('Idade: ', idade)
        print('*'*40)
except FileNotFoundError:



#Função Alterar Dados
def alterar_dados():
    #Abrir o arquivo 'Dados.txt' em modo de leitura ('r')
    with open('Dados.txt', 'r') as arquivo:
        #Ler todas as linhas do arquivo e armazená-las em uma lista
        linhas= arquivo.readlines()
        #Verificar se não há linhas (dados) no arquivo
        if not linhas:
        print('Nenhum dado de aluno cadastrado,')
        return
        #Solicitar ao usuário o nome do aluno que deseja alterar
        if int(dados[0]) == nome
        #precisa finalizar


#Função Excluir Registro
def excluir_cadastro():
    #Abrir o arquivo 'Dados.txt' em modo de leitura ('r')
    with open('Dados.txt', 'r') as arquivo:
        #Ler todas as linhas do arquivo e armazená-las em uma lista
        linhas= arquivo.readlines()
        #Verificar se não há linhas (dados) no arquivo
        if not linhas:
        print('Nenhum dado de aluno cadastrado,')
        return
    nome= str

    with open('Dados.txt','w') as arquivo:


#Função Fazer Backup
def fazer_backup