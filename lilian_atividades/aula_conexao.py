import sqlite3 as conector

# Abertura de conexão
conexao = conector.connect("primeiro_banco_sqlite")

# Aquisição de um cursor
cursor = conexao.cursor()

# Execução comandos: SELECT ... CRATE ...
cursor.execute("CREATE TABLE pessoas(nome text, idade integer, email text)")

cursor.fetchall()

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()