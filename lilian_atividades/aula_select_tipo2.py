import sqlite3 as conector
from principal_molelo import Pessoa

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("lilian_atividades/banco_dados_exemplo2.db") 
cursor = conexao.cursor()

# Definição dos comandos
comando = '''SELECT * FROM pessoa WHERE oculos= :usa_oculos;'''
cursor.execute(comando, {"usa_oculos": True})

# Recuperação dos registros
registros = cursor.fetchall()
for registro in registros:
    pessoa= Pessoa(*registro)
    print("cpf:", type(pessoa.cpf), pessoa.cpf)
    print("nome:", type(pessoa.nome), pessoa.nome)
    print("nascimento:", type(pessoa.usa_oculos), pessoa.usa_oculos)


# Fechamento das conexões
cursor.close()
conexao.close()