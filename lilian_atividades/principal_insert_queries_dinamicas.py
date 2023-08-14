import sqlite3 as conector
from principal_molelo import Pessoa

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("lilian_atividades/banco_dados_exemplo2.db")
cursor = conexao.cursor()

# Criação de umobjeto do tipo Pessoa
pessoa = Pessoa(10000000099, 'Maria','1990-01-31',False)

# Definição de um comando com query parameter
comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (?,?,?,?);'''
cursor.execute(comando, (pessoa.cpf, pessoa.nome, pessoa.data_nascimento, pessoa.usa_oculos))

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()