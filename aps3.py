#   Programa de criptografia de chave simétrica na qual utiliza a tabela
# UNICODE como referêrencia para a cifragem. O cálculo é realizado somando
# ou subtraíndo a chave com a numeração UNICODE dos caracteres da mensagem, 
# e convertendo novamente em caracteres.
#   O script consiste 2 procedimentos, 2 funções, 2 variáveis globais e um 
# total de 5 variáveis locais.

def checar_e_cripto():
    # Impede o usuário de digitar uma quantidade de caracteres maior do que 128.
    while True:
        texto = input('\nDigite o texto:\n>>> ')
        if len(texto) <= 128:
            esconde(texto)
            break
        else:
            print('Limite de 128 caracteres ultrapassado!')
    return

# Procedimento "esconde" realiza a criptografia da mensagem, recebendo o texto
# digitado como parâmetro.
def esconde(msg):
    txt = ''
    for c in msg:
        # O comando "ord" transfoma o caracter "c" da palavra em seu códico UNICODE e
        # soma com o valor da chave, e o comando "chr" transforma o resultado de
        # volta em caracter e junta com a variável "txt".
        txt += chr(ord(c) + chave)
    print('\nMensagem codificada:\n', txt)
    arquivo = open('documento.txt', 'w', encoding = 'utf-8')
    arquivo.write(txt)
    arquivo.close()
    print('\nMensagem criptografada e armazenada no arquivo "documento.txt".',)
    return txt

# Procedimento "mostra" realiza a descriptografia da mensagem, fazendo a operação inversa
# da função "esconde".
def mostra():
    # Abre "documento.txt" para leitura.
    arquivo=open('documento.txt', 'r', encoding = 'utf-8')
    txt = ''
    for c in arquivo.readline():
        txt += chr(ord(c) - chave)
    arquivo.close()
    print('\nMensagem decodificada:\n', txt)
    return

# Função que verifica se o que foi digitado é um número inteiro, maior que -33 e menor
# que 1.113.881 evitando o erro de valor inválido caso o usuário digite um
# valor diferente.
def checarInteiro():
    print('\nDigite o valor da chave que você deseja utilizar:')
    while True:
        try:
            v = int(input('>>> '))
            if v > -33 and v < 1113881:
                return v
            else:
                print('Digite um valor maior que -33 e menor que 1.113.881')
        except ValueError:
            print('\nValor inválido, digite um número inteiro qualquer!')

# Início do script.
print('''Bem vindo ao programa de criptografia!
Escolha um número inteiro que será usado como chave para cifrar, e o mesmo valor para decifrar.''')
chave = checarInteiro()
# Menu das opções.
print('''
    +-------------------------+
    |   Menu                  |   
    |   0:  Sair              |
    |   1:  Criptografia      |
    |   2:  Descriptografia   |
    |   3:  Trocar Chave      |
    +-------------------------+
''')
# Impede o usuário de digitar um valor diferente dos que foram aprensentados.
while True:
    opcao = input('|>>> ')
    if opcao == '0':
        break
    elif opcao == '1':
        # CRIPTOGRAFAR
        checar_e_cripto()
        break
    elif opcao == '2':
        # DESCRIPTOGRAFAR
        mostra()
        break
    elif opcao == '3':
        chave = checarInteiro()
    else:
        print('\nOpção inválida!')
input('Obrigado por utilizar o nosso programa de criptografia!')
# Fim do script.