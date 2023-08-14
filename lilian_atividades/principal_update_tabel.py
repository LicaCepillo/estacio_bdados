import sqlite3 as conector

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("lilian_atividades/banco_dados_exemplo2.db")
cursor = conexao.cursor()

# Definição dos comandos UPDATE
comando1 = '''UPDATE pessoa SET oculos = 1;'''
cursor.execute(comando1)

comando2 = '''UPDATE pessoa SET oculos = ? WHERE cpf =10000000099;'''
cursor.execute(comando2, (False,))

comando3 = '''UPDATE pessoa SET oculos = :usa_oculos WHERE cpf= :cpf;'''
cursor.execute(comando3,{"usa_oculos": False, "cpf": 20000000099})

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()