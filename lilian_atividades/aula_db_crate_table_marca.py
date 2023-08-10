import sqlite3 as conector

# Abertura da conexão e aquisição do cursor
conexao = conector.connect('lilian_atividades/banco_dados_exemplo2.db')
cursor = conexao.cursor()

# Execução de um comando: CREATE TABLE 
comando = '''CREATE TABLE Marca(
            id INTEGER NOT NULL,
            nome TEXT NOT NULL,
            sigla CHARACTER(2) NOT NULL,
            PRIMARY KEY (id)
);'''

cursor.execute(comando)

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()
