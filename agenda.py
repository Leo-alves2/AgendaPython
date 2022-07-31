'''
Programa de agenda desenvolvido em Python, utilizando Função, While, For, If,
lista e Dicionários.

Os dados serão gravados e carregados de um arquivo texto
'''
# Funções que será invocada conforme seja selecionado pelo usuário


from agenda_binary import salvar_contatos


def carregar_contatos():

    # Criando uma lista vazia

    lista = []

    # Utilizando o Try e except para evitar erro de o arquivo não existir

    try:
        # Abrindo o arquivo como leitura

        arquivo = open('contatos.txt', 'r')

        # Utilizando o FOR com a função readlines que ler linha  por linha,
        # conseguimos pegar a linha completa

        for linha in arquivo.readlines():

            # Utilizando a função split conseguimos passar o delimitador e
            # transformar em um vetor de colunas
            # Utilizando a função strip para remover os espaços em branco do
            # inicio e fim da string, não remover interno
            # Obs. Strip em python é igual a Trim em outras linguagem

            coluna = linha.strip().split(';')

            # Pegando cada coluna e adicionando ao dicionario da
            # lista de contato

            contato = {
                'tel': coluna[2],
                'nome': coluna[0],
                'email': coluna[1]
            }
            # Adicionando na lista dos dicionários

            lista.append(contato)

        # Todo arquivo aberto precisa ser fechado

        arquivo.close()

    # Tratando o erro se não tiver o arquivo criado

    except FileNotFoundError:
        pass

    # Retornar a lista para ser carregado pelo programa

    return lista


def existe_contato(lista, tel):

    # Verificar se tem contato cadastrado

    if len(lista) > 0:

        # Utilizando o For para correr toda a lista e buscar por
        # telefone igual ao digitado, só entra aqui se for maior que 0

        for contato in lista:
            if contato['tel'] == tel:
                return True

    # Igual a zero retorna false direto

    return False


def adicionar(lista):

    # Será utilizada com chave única do sistema e vamos
    #  utilizar o while para verificar se existe cadastrado

    while True:
        tel = input('Digite o telefone do contado: ')

        # Vamos verificar se existe o telefone no sistema

        if not existe_contato(lista, tel):
            break
        else:
            print('Este telefone já foi utilizado.')
            print('Por favor, tente um novo telefone.')

    # Se o telefone não existir
    # Criamos um dicionario com os dados

    contato = {
        'tel': tel,
        'nome': input('Digite o nome: '),
        'email': input('Digite o email: ')
    }

    # Adicionar o dicionário na lista

    lista.append(contato)

    print('O contato {} foi cadastrado com sucesso!\n'.format(contato['nome']))


def alterar(lista):

    # Para estilizar a impressão

    print('======== Alterar Contato ========')

    # Verificar se tem algum contato cadastrado

    if len(lista) > 0:

        # Pegar o que foi digitado pelo usuário

        tel = input('Digite o telefone do contato: ')

        # Verificar se existe o contato cadastrado

        if existe_contato(lista, tel):

            # Se existir o contato ele mais pegar e imprimir na tela

            for contato in lista:
                if contato['tel'] == tel:
                    print('Nome: {}'.format(contato['nome']))
                    print('Email: {}'.format(contato['email']))
                    print('Telefone: {}'.format(contato['tel']))
                    print('=========================================\n')

                    contato['nome'] = input('Digite o novo nome do contato: ')
                    contato['email'] = input(
                        'Digite o novo Email do contato: ')

                    print('Os dados do contato de telefone {},\
                        foram alterados com sucesso!'.format(contato['tel']))

                    break

        else:
            print(
                'Não existe contato cadastro no sistema com este telefone {}\n'
                .format(tel))
    else:
        print('Não existe contato cadastrado no sistema.\n')


def excluir(lista):

    # Para estilizar a impressão

    print('======== Excluir Contato ========')

    # Verificar se tem algum contato cadastrado

    if len(lista) > 0:

        # Pegar o que foi digitado pelo usuário

        tel = input('Digite o telefone do contato para ser excluído: ')

        # Verificar se existe o contato cadastrado

        if existe_contato(lista, tel):

            # Se existir o contato ele mais pegar e imprimir na tela

            for i, contato in enumerate(lista):
                if contato['tel'] == tel:
                    print('Nome: {}'.format(contato['nome']))
                    print('Email: {}'.format(contato['email']))
                    print('Telefone: {}'.format(contato['tel']))
                    print('=========================================\n')

                    del lista[i]

                    print('Contato foi apagado com sucesso!\n')
                    break

        else:
            print(
                'Não existe contato cadastro no sistema com este telefone {}\n'
                .format(tel))
    else:
        print('Não existe contato cadastrado no sistema.\n')


def buscar(lista):

    # Para estilizar a impressão

    print('======== Buscar Contato ========')

    # Verificar se tem algum contato cadastrado

    if len(lista) > 0:

        # Pegar o que foi digitado pelo usuário

        tel = input('Digite o telefone do contato: ')

        # Verificar se existe o contato cadastrado

        if existe_contato(lista, tel):

            # Se existir o contato ele mais pegar e imprimir na tela

            for contato in lista:
                if contato['tel'] == tel:
                    print('Nome: {}'.format(contato['nome']))
                    print('Email: {}'.format(contato['email']))
                    print('Telefone: {}'.format(contato['tel']))
                    print('=========================================\n')
                    break

        else:
            print(
                'Não existe contato cadastro no sistema com este telefone {}\n'
                .format(tel))
    else:
        print('Não existe contato cadastrado no sistema.\n')


def listar(lista):

    # Para estilizar a impressão

    print('======== Listar Contatos ========')

    # Verificar se tem algum contato cadastrado

    if len(lista) > 0:

        # Percorrer a lista com o for e colocar o numere da sequencia

        for i, contato in enumerate(lista):
            print('Contato {}:'.format(i+1))  # O +1 é para não começar do zero
            # O \t é para tabular a direita e como nossos dados é dicionario
            #  precisamos passar a chave
            print('\tNome: {}'.format(contato['nome']))
            print('\tEmail: {}'.format(contato['email']))
            print('\tTelefone: {}'.format(contato['tel']))

            # Para estilizar a impressão

            print('=========================================')

        # Imprimindo a quantidade de contato da lista

        print('Quantidade de contatos: {}\n'.format(len(lista)))
    else:
        print('Não existe contato cadastrado no sistema.\n')


# Iniciar o programa e printar o menu na tela

def principal():

    # Carregando o arquivo para lista

    lista = carregar_contatos()

    # Colocando o código no loop infinito para fica sempre
    #  ativo na tela do usuário

    while True:

        # Para estilizar a impressão

        print('======== Agenda Telefônica ========')

        # Printar as opções

        print(' 1 - Adicionar Contato')
        print(' 2 - Alterar Contato')
        print(' 3 - Excluir Contato')
        print(' 4 - Buscar Contato')
        print(' 5 - Listar Contato')
        print(' 6 - Sair do Programa')

        # Pegando o que esta sendo digitado pelo usuário

        opção = int(input('>'))

        # Selecionando a função conforme digitação do usuário

        if opção == 1:
            adicionar(lista)
            salvar_contatos(lista)
        elif opção == 2:
            alterar(lista)
            salvar_contatos(lista)
        elif opção == 3:
            excluir(lista)
            salvar_contatos(lista)
        elif opção == 4:
            buscar(lista)
        elif opção == 5:
            listar(lista)
        elif opção == 6:
            print('Saindo do programa...')

            # Para sair do programa

            break

        # Caso não seja selecionado nenhuma das opções
        # vai imprimir uma mensagem na tela

        else:
            print('Opção inválida. Por favor, tente novamente.')


# Invocar o programa para inicializar

principal()
