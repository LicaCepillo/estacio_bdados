import sqlite3 as conector

# Abertura de conexão e aquisição de cursor
conexao = conector.connect('lilian_atividades/banco_dados_exemplo2.db')
cursor = conexao.cursor()

# Execução de um comando ALTER
comando = '''ALTER TABLE Veiculo
                ADD motor REAL;'''

cursor.execute(comando)

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()
