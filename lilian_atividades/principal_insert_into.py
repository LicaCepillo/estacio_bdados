import sqlite3 as conector

# Abertura de conexão e aquisiçáo de cursor
conexao = conector.connect("lilian_atividades/banco_dados_exemplo2.db")
cursor = conexao.cursor()

# Execução de um comando: INSERT INTO
comando = '''INSERT INTO pessoa (cpf, nome, nascimento, oculos)
        VALUES (12345678900, 'João','2000-01-31', 1);'''

cursor.execute(comando)

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()
