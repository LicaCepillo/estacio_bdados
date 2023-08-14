import sqlite3 as conector
from principal_molelo import Pessoa

# Abertura de conexão e aquisisção de cursor
conexao = conector.connect("lilian_atividades/banco_dados_exemplo2.db")
cursor = conexao.cursor()

# Criação de um objeto do tipo Pessoa
pessoa = Pessoa(20000000099, 'José','1990-02-28', False)

# Definição de um comando com query parameter
comando = '''INSERT INTO Pessoa (cpf, nome, nascimento,oculos)
                VALUES (:cpf,:nome,:data_nascimento,:usa_oculos);'''
cursor.execute(comando, {"cpf": pessoa.cpf,
                         "nome": pessoa.nome,
                         "data_nascimento": pessoa.data_nascimento,
                         "usa_oculos":pessoa.usa_oculos})

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()