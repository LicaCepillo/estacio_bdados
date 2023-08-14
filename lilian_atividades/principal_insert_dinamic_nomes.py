import sqlite3 as conector
from principal_molelo import Pessoa

# Abertura de conexão e aquisição de cursos
conexao = conector.connect("lilian_atividades/banco_dados_exemplo2.db")
cursor = conexao.cursor()

# Criação de um objeto do tipo Pessoa
pessoa = Pessoa(30000000999, 'Silva', '1998-03-30', True)

# Definição de um comando dom named parameter
comando = '''INSERT INTO Pessoa VALUES(:cpf,:nome,:data_nascimento,:usa_oculos);'''
cursor.execute(comando, vars(pessoa))
print(vars(pessoa))

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()