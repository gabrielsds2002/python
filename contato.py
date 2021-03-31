agenda=[]
def pede_nome():
    return (input("Digite um nome: "))
def pede_nome_arquivo():
        return (input("Digite um nome de arquivo: "))
def pede_telefone():
    return(input("Digite um telefone: "))

def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None

def novo():
    global agenda
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome,telefone])

def lista():
    agenda.sort()
    print("\nAgenda \n\n -------------")
    for e in agenda:
        print("Nome: %s Telefone: %s" % (e[0], e[1]))    
    print("----------\n")

def apagar():
    global agenda
    nome = pede_nome()
    p = pesquisa(nome)
    if p!= None:
        del agenda[p]
    else:
        print("Nome não encontrado!")
        
def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if valor >= inicio and valor <= fim:
                return(valor)
            else:
                print("Valor invalido!")
        except ValueError:
            print("Valor invalido!")

def le():
    global agenda
    nome_arquivo = pede_nome_arquivo()
    arquivo = open(nome_arquivo,"r", encoding="utf-8")
    agenda=[]
    for l in arquivo.readlines():
        nome, telefone = l.strip().split("#")
        agenda.append([nome, telefone])
    arquivo.close()

def gravar():
    nome_arquivo = pede_nome_arquivo()
    arquivo = open(nome_arquivo, "w", encoding="utf-8")
    for e in agenda:
        arquivo.write("%s#%s\n" % (e[0],e[1]))
    arquivo.close()
        
def altera():
    p = pesquisa(pede_nome())
    if p!=None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print("Nome encontrado!")
        nome = pede_nome()
        telefone = pede_telefone()
        agenda[p]=[nome, telefone]
    else:
        print("Nome não encontrado!")
        
def menu():    
    print("""
            1 - Novo Contato   
            2 - Alterar Contato
            3 - Apagar Contato 
            4 - Listar Contatos
            5 - Gravar Arquivo
            6 - Le Arquivo
            0 - Sair           
            """)
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 6)

while True:
    opcao = menu()
    if opcao == 0:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        altera()
    elif opcao == 3:
        apagar()
    elif opcao == 4:
        lista()
    elif opcao == 5:
        gravar()
    elif opcao == 6:
        le()
