import json

#Função pegar os dados do arquivo json
#Pegar dados
def pegardados():
    #Essa função tentará buscar um arquivo Dados.txt
    try:
        with open('Dados.txt', 'r') as arquivo:
        # Inicializar uma lista para armazenar os dados dos alunos
            return json.load(arquivo)
    #Caso a função não encontre o arquivo Dados.txt ela retornará um dicionário vazio
    except Exception as e:
        return {}


#Função Cabeçalho
def cabecalho():
#cabecalho
    print('*'*64)
    print('*************************FACULDADE CESUSC***********************')
    print()
    print('CURSO: ANÁLISE E DESENVOLVIMENTO DE SISTEMAS')
    print('Discipl.: LÓGICA DE PROG E ALGORÍTMOS')
    print('Turma: ADS: 11 / Ano: 2024')
    print('Prof. Roberto Fabiano Fernandes')
    print('Aluno: Leonardo Flores')
    print('Avaliação: N2/N3')
    print()
    print('*'*64)
    print()
    

#Função Menu
def menu():
#menu
    while True:
        print()
        print('*'*64)
        print()
        print('Bem vindos ao CR Flamengo!')
        print('Menu de escolha de opções: ')
        print('1 - Cadastrar Dados')
        print('2 - Listar Dados')
        print('3 - Alterar Dados')
        print('4 - Excluir Dados')
        print('5 - Realizar Backup do arquivo')
        print('0 - Sair')
        print()
        opcao= input('Digite uma opção aqui: ')
        print()
        print('*'*64)
        if opcao== '1':
            print()
            print('*'*64)
            print()
            print('Opção 1: ')
            cadastrar()
        elif opcao== '2':
            print()
            print('*'*64)
            print()
            print('Opção 2: ')
            listar()
        elif opcao== '3':
            print()
            print('*'*64)
            print()
            print('Opção 3: ')
            alterar()
        elif opcao== '4':
            print()
            print('*'*64)
            print()
            print('Opção 4: ')
            excluir()
        elif opcao== '5':
            print()
            print('*'*64)
            print()
            print('Opção 5: ')
            fazer_backup()
        elif opcao== '0':
            break    
        else:
            print('*'*64)
            print()
            print('Opção inválida, digite um número conforme as oções mencionadas')
            print()
            print('*'*64)
            print()


#Função Cadastrar
def cadastrar():
#Cadastrar
    #DÚVIDA: por quê usar o try nessa função
    try:
        #Solicitar ao usuário as informações do aluno
        print()
        print('*'*64)
        print()
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
        
    #Gerador de IDs
    #Pega o maior ID e adiciona 1       
        #Variável utilizada com a finalidade do primeiro ID ser 1
        #
        alunoid=0
        if alunos:
            for id in alunos.keys():
                if int(id)>int(alunoid):
                    alunoid=id
        alunoid=int(alunoid)+1
        #Adiciona o ID gerado como chave em json "na memória do sistema"
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
        #Grava o arquivo json "da memória do sistema" em um arquivo Dados.txt
        #Caso não tenha um arquivo Dados.txt ele será criado neste momento
        with open('Dados.txt', 'w') as arquivo:
            json.dump(alunos, arquivo)        

        #Exibir uma mensagem de sucesso
        print()
        print('*'*64)
        print()
        print('Dados do(a) aluno(a) cadastrados com sucesso!')
        print('O ID do aluno ', nomealuno, ' é: ', alunoid)
        print()
        print('*'*64)
        print()
    except ValueError:
        #Capturar um erro caso os valores fornecidos pelo usuário não estejam no formato esperado
        print('Valor inválido. Verifique as informações e tente novamente')
    except Exception as e:
        #Capturar qualquer outro erro que possa ocorrer durante o cadastro dos dados
        print('Ocorreu um erro ao cadastrar os dados:', str(e))


# Função Listar
#Listar dados
def listar():
    try:
        alunos= pegardados()
        #Ler cada linha do arquivo
        if alunos:
            for alunoid, dados in alunos.items():               
                #Imprimir os dados dos alunos
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
        else:
            print()
            print('*'*64)
            print()
            print('Nenhum dado cadastrado')
            print()
            print('*'*64)
            print()
    except FileNotFoundError:
        print(f'Arquivo Dados.txt não encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

#Função Alterar Dados
#Alterar dados
def alterar():
    alunos=pegardados()
    for alunoid, dados in alunos.items():
        print(alunoid, " ", dados['Nome do aluno'])
        
    alteraraluno = input('Digite o ID do aluno: ')
    print('ID selecionado: ', alteraraluno)
    #Verificar a existência do ID informado pelo usuário dentro de Dados.txt
    existAluno = False
    #Para tanto, o "for" irá percorrer todos os "alunoid" dentro do Dados.txt
    for alunoid, dados in alunos.items():
        if int(alunoid) == int(alteraraluno):
            existAluno = True
            break
    #Caso o ID não exista cairá no else abaixo.
    #Caso o ID exista abrirá novamente os todos os campos para a alteração
    #OBS: Todos os campos deverão ser preenchidos novamente
    #Os dados serão sobrescritos no ID mencionado        
    if existAluno:
        print('Digite todos os campos')
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
        
    #Alterando a classe de alteraralunos para string
    #Passo necessário para salvar no Dados.txt
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
        #Escrevendo os dados no arquivo Dados.txt
        with open('Dados.txt', 'w') as arquivo:
            json.dump(alunos, arquivo)
            print('*'*64)
            print()
            print('Os dados do aluno de ID', alteraraluno,'foram alterados com sucesso!' )
            print()
            print('*'*64)
    else:
        print()
        print('*'*64)
        print()
        print('ID inválido, por gentileza, verifique o caracter informado.')
        print()
        print('*'*64)
        print()
    
#Função Excluir Registro
def excluir():
    try:
        alunos=pegardados()

        for alunoid, dados in alunos.items():
            print(alunoid, " ", dados['Nome do aluno'])
        excluirid = input('Digite o ID do aluno a ser excluído: ')
        if excluirid in alunos.keys():
            print('ID existente.')
            alunos.pop(excluirid)
            print(f'O aluno de ID', {excluirid}, 'foi excluído com sucesso.') 
            #Escrevendo os dados no arquivo Dados.txt
            with open('Dados.txt', 'w') as arquivo:
                json.dump(alunos, arquivo)             
        else:
            print('Opção inválida, digite um ID conforme as oções informadas')
        #s_ou_n_excluirid = input('Tem certeza que desea excluir o aluno de ID: ', excluirid, '? Digite "s" para confirmar a exclusão ou "n" para canelar a operação.')
    except ValueError:
        print("Valor inválido. Certifique-se de digitar um valor numérico para o código do aluno.")
    except Exception as e:
        print("Ocorreu um erro ao excluir os dados:", str(e))

#Função Fazer Backup
def fazer_backup():
    try:
        alunos=pegardados()
        with open('Dados_Backup.txt','w') as backup:
            json.dump(alunos, backup)
        print()
        print('*'*64)
        print()
        print('Backup do arquivo realizado com sucesso!')
        print()
        print('*'*64)
        print()
    except FileNotFoundError:
        print('O arquivo Dados.txt não foi encontrado.')
    except Exception as e:
        print('Ocorreu um erro ao realizar o backup: ', str(e))
