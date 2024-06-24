import json

#Função Cabeçalho
def cabecalho():
#cabecalho
    print('*'*44)
    print('***************FACULDADE CESUSC*************')
    print('CURSO: ANÁLISE E DESENVOLVIMENTO DE SISTEMAS')
    print('Discipl.: LÓGICA DE PROG E ALGORÍTMOS')
    print('Turma: ADS: 11 / Ano: 2024')
    print('Prof. Roberto Fabiano Fernandes')
    print('Aluno: Leonardo Flores')
    print('Avaliação: N2/N3')
    print('*'*44)
    

#Função Menu
def menu():
    #menu
    while True:
        print('Bem vindos ao CR Flamengo!')
        print('Menu de escolha de opções: ')
        print('1 - Cadastrar Dados')
        print('2 - Listar Dados')
        print('3 - Alterar Dados')
        print('4 - Excluir Dados')
        print('5 - Realizar Backup do arquivo')
        print('0 - Sair')
        opcao= input('Digite uma opção aqui: ')
    
        if opcao== '1':
            print('Opção 1: ')
            cadastrar()
        elif opcao== '2':
            print('Opção 2: ')
            listar()
        elif opcao== '3':
            print('Opção 3: ')
            alterar()
        elif opcao== '4':
            print('Opção 4: ')
            excluir()
        elif opcao== '5':
            print('Opção 5: ')
          #  realizar_backup()
        elif opcao== '0':
            break    
        else:
            print('Opção inválida, digite um número conforme as oções mencioandas')


#Função Cadastrar
def cadastrar():
    try:
        #Solicitar ao usuário as informações do aluno
        nomealuno = input('Informe o nome do(a) aluno(a): ')    
        idadealuno = input('Informe a idade do(a) aluno(a): ')
        sexoaluno = input('Informe o sexo do(a) aluno(a) (masculino ou feminino): ')
        nomeresponsavel = input('Informe o nome do(a) responsável pelo(a) aluno(a): ')
        telefone = input('Informe o telefone do(a) responsável: ')
        cpfresponsavel = input('Informe o CPF do(a) responsável: ')
        endereco = input('Informe seu endereço: ')
        cidade = input('Informe sua cidade: ')
        estado = input('Informe seu Estado: ') 
        cep = input('Informe o seu CEP: ')

        alunos=pegardados()
        print(alunos)
        #Gerador de IDs
        #Pega o maior ID e adiciona 1       
        alunoid=0
        if alunos:
            for id in alunos.keys():
                if int(id)>int(alunoid):
                    alunoid=id
        alunoid=int(alunoid)+1

        print(alunoid)
        #Adiciona o ID gerado na chave json
        alunos[str(alunoid)]={
                'Nome do aluno' :nomealuno,
                'Idade do aluno': idadealuno,
                'Sexo do aluno': sexoaluno,
                'Nome do responsável': nomeresponsavel,
                'Telefone do responsável': telefone,
                'CPF do responsável': cpfresponsavel,
                'Endereço': endereco,
                'Cidade': cidade,
                'Estado': estado,
                'CEP':cep
        
                }
        
        with open('Dados.txt', 'w') as arquivo:
            json.dump(alunos, arquivo)
        

        #Exibir uma mensagem de sucesso
        print('*'*44)
        print()
        print('Dados do(a) aluno(a) cadastrados com sucesso!')
        print('O ID do aluno ', nomealuno, ' é: ', alunoid)
        print()
        print('*'*44)
        print()
    except ValueError:
        #Capturar um erro caso os valores fornecidos pelo usuário não estejam no formato esperado
        print('Valor inválido. Verifique as informações e tente novamente')
    except Exception as e:
        #Capturar qualquer outro erro que possa ocorrer durante o cadastro dos dados
        print('Ocorreu um erro ao cadastrar os dados:', str(e))

#Função pegar os dados do arquivo json
def pegardados():
    try:
        with open('Dados.txt', 'r') as arquivo:
        # Inicializar uma lista para armazenar os dados dos alunos
            return json.load(arquivo)
    except Exception as e:
        return {}


# Função Listar
def listar():
    try:
        alunos= pegardados()
        # Ler cada linha do arquivo
        for alunoid, dados in alunos.items():

            # Imprimir os dados dos alunos
            print()
            print('*' * 40)
            print('Aluno ID: ', alunoid)
            print('Nome do aluno: ', dados['Nome do aluno'])
            print('Idade do aluno: ', dados ['Idade do aluno'])
            print('Sexo do aluno: ', dados['Sexo do aluno'])
            print('Nome do responsável: ', dados['Nome do responsável'])
            print('Telefone do responsável: ', dados['Telefone do responsável'])
            print('CPF do responsável: ', dados['CPF do responsável'])
            print('Endereço: ', dados['Endereço'])
            print('Cidade: ', dados['Cidade'])
            print('Estado: ', dados['Estado'])
            print('CEP: ', dados['CEP'])
            print('*' * 40)
            print()

    except FileNotFoundError:
        print("Arquivo 'Dados.txt' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    

# #Função Alterar Dados
def alterar():
    alunos=pegardados()

    for alunoid, dados in alunos.items():
        print(alunoid, " ", dados['Nome do aluno'])

    alteraraluno = input('Digite o ID do aluno: ')
    print('ID selecionado: ', alteraraluno)

    existAluno = False
    for alunoid, dados in alunos.items():
        if int(alunoid) == int(alteraraluno):
            existAluno = True
        
    if existAluno:
        nomealuno = input('Informe o nome do(a) aluno(a): ')    
        idadealuno = input('Informe a idade do(a) aluno(a): ')
        sexoaluno = input('Informe o sexo do(a) aluno(a) (masculino ou feminino): ')
        nomeresponsavel = input('Informe o nome do(a) responsável pelo(a) aluno(a): ')
        telefone = input('Informe o telefone do(a) responsável: ')
        cpfresponsavel = input('Informe o CPF do(a) responsável: ')
        endereco = input('Informe seu endereço: ')
        cidade = input('Informe sua cidade: ')
        estado = input('Informe seu Estado: ') 
        cep = input('Informe o seu CEP: ')

        alunos[str(alteraraluno)]={
                'Nome do aluno' :nomealuno,
                'Idade do aluno': idadealuno,
                'Sexo do aluno': sexoaluno,
                'Nome do responsável': nomeresponsavel,
                'Telefone do responsável': telefone,
                'CPF do responsável': cpfresponsavel,
                'Endereço': endereco,
                'Cidade': cidade,
                'Estado': estado,
                'CEP':cep
        
                }
        
        with open('Dados.txt', 'w') as arquivo:
            json.dump(alunos, arquivo)
        

    else:
        print("Aluno seleconado n existe.")
            


# #Função Excluir Registro
# def excluir():
#ao inves do dump usar o outro codigo para tirarr o json

#del
# #Função Fazer Backup
# def fazer_backup
