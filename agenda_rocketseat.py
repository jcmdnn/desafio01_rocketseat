def cadastrar_contato(nome, telefone, email):
    contato = {"nome": nome, "telefone": telefone, "email": email}
    contatos.append(contato)
    print(f"\n\nO contato {nome} foi adicionado com sucesso. ")
    
def listar_contatos(contatos):
    print("\nContatos: \n")
    for contato in contatos:
        print(f"Nome: {contato['nome']} | ☏  Telefone: {contato['telefone']} | ✉  Email: {contato['email']}")
    return
        

def editar_contatos():
    pass

def listar_favoritos():
    pass

def deletar_contatos():
    pass

contatos = []

while True:
    print("\n----------------- CONTATOS -----------------\n")
    print("1. Adicionar Contato: ")
    print("2. Lista de Contatos: ")
    print("3. Editar Contato: ")
    print("4. Lista de Contatos Favoritos: ")
    print("5. Excluir Contato: ")
    print("6. Sair ")
    print("\n--------------------------------------------\n")

    opcao_lista = int(input("Digite a opção desejada: "))

    if opcao_lista == 1:
        nome = input("Digite o nome do contato: ")
        telefone = int(input("Digite o número de telefone: "))
        email = input("Digite o email: ")
        cadastrar_contato(nome, telefone, email)

    elif opcao_lista == 2:
        listar_contatos(contatos)

    elif opcao_lista == 3:
        pass

    elif opcao_lista == 4:
        pass

    elif opcao_lista == 5:
        pass

    elif opcao_lista == 6:
        break