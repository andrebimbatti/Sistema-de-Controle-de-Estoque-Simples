import sqlite3
import os


def limpar():
    os.system('cls')

def esperar():
    input("Pressione Enter para continuar")

def titulo(titulo):
    estrela = '*'
    print(estrela * 50)
    print(f":: {titulo} ::")
    print(estrela * 50, '\n\n')

def conectar():
    conn = sqlite3.connect("estoque.db")
    return conn

def tabela_estoque():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY,
        nome TEXT,
        quantidade INTEGER
        )
        """
    )

def cadastrar():
    limpar()
    titulo('CADASTRAR MERCADORIA NOVA')
    while True:
        nome = input("Digite o nome do Produto ou deixe vazio para voltar ao menu:\n")
        if nome == "":
            print("")
            return
        else:
            break

    while True:
        try:
            quantidade = int(input("Digite a quantidade:\n"))
            
            if quantidade <= 0:
                print("A quantidade precisa ser maior ou igual a 0")
            else:
                break

        except ValueError:
            print("❌ Digite um valor para quantidade valido")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
            INSERT INTO produtos(nome, quantidade)
            VALUES(?,?)
        """,(nome, quantidade)
    )
    conn.commit()
    conn.close()

def entrada_de_produtos(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT quantidade FROM produtos WHERE id = ?", (id,))

    resultado = cursor.fetchone()

    if resultado == None:
        print("❌ Produto não encontrado!")
        conn.close()
        return
    
    quantidade_atual = resultado[0]

    while True:
        try:
            quantidade = int(input("Digite a quantidade que deseja adicionar:\n"))
            
            if quantidade <= 0:
                print("A quantidade precisa ser maior ou igual a 0")
            else:
                break

        except ValueError:
            print("❌ Digite um valor para quantidade valido")

    nova_quantidade = quantidade_atual + quantidade

    cursor.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (nova_quantidade, id))
    conn.commit()
    conn.close()
    print("✅ Nova quantidade atualizada com sucesso!")
    input("Pressione Enter para continuar")

def saida(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT quantidade FROM produtos WHERE id = ?",(id,))

    resultado = cursor.fetchone()

    if resultado == None:
        print("❌ Produto não encontrado!")
        conn.close()
        return
    
    quantidade_atual = resultado[0]

    while True:
        try:
            quantidade = int(input("Digite a quantidade que deseja remover:\n"))
            
            if quantidade <= 0:
                print("A quantidade precisa ser maior ou igual a 0")
            else:
                break

        except ValueError:
            print("❌ Digite um valor para quantidade valido")

    nova_quantidade = quantidade_atual - quantidade

    cursor.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (nova_quantidade, id))
    conn.commit()
    conn.close()
    print("✅ Nova quantidade atualizada com sucesso!")
    input("Pressione Enter para continuar")

def exibir_estoque():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produtos")
    conn.commit()

    produtos = cursor.fetchall()
    print(f'{"ID":5} | {"PRODUTO":50} | {"QUANTIDADE":7}')
    for produto in produtos:
        print(f'{produto[0]:5} | {produto[1]:50} | {produto[2]:7}') 
    
    conn.close()
    esperar()
    
def deletar_produto(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
            DELETE FROM produtos
            WHERE id = ?
        """, (id,)
    )
    print(f'Produto do id {id} foi deletado com sucesso.')
    conn.commit()
    conn.close()

def menu():
    while True:
        limpar()
        titulo('CONTROLE DE MERCADORIA')
        
        print(
            '1 - CADASTRAR PRODUTO \n' \
            '2 - ENTRADA DE PRODUTOS \n' \
            '3 - SAIDA DE PRODUTOS \n' \
            '4 - LISTAR ESTOQUE \n' \
            '5 - DELETAR PRODUTO \n' \
            '6 - SAIR')
        entrada = input("Digite o número da opção que deseja acessar: ")
        if entrada == '':
            continue
        opcao = int(entrada)

        match opcao:
            case 1:
                cadastrar()
            case 2:
                limpar()
                titulo('ENTRADA DE PRODUTOS')
                exibir_estoque()
                entrada = input('Digite o id do produto que deseja dar entrada ou deixe vazio para sair:\n ')
                if entrada == '':
                    continue
                id = int(entrada)
                entrada_de_produtos(id)
            case 3:
                limpar()
                titulo('SAIDA DE PRODUTOS')
                exibir_estoque()
                entrada = input('Digite o id do produto que deseja dar saida ou deixe vazio para sair:\n: ')
                if entrada == '':
                    continue
                id = int(entrada)
                
                saida(id)
            case 4:
                limpar()
                titulo('ESTOQUE DE PRODUTOS')
                exibir_estoque()
            case 5:
                limpar()
                titulo('DELETAR PRODUTO')
                exibir_estoque()
                entrada = input('Digite o id do produto que deseja remover ou deixe vazio para sair:\n: ')
                if entrada == '':
                    continue
                id = int(entrada)
                deletar_produto(id)

            case 6:
                print('Obrigado por usar nosso software!')
                print('Software desenvolvido por: Andre Bimbatti')
                break
            case _:
                print("Você nao digitou um numero de opcao válida")
