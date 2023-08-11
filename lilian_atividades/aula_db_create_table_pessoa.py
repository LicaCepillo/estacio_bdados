import sqlite3 as conector

try:
    # Abertura de conexão e aquisição de cursor

    conexao = conector.connect('lilian_atividades/banco_dados_exemplo2.db')
    cursor = conexao.cursor()

    # Execução de um comando
    comando = '''CREATE TABLE Pessoa (
        cpf INTERGER NOT NULL,
        nome  TEXT NOT NULL,
        nascimento DATE NOT NULL,
        oculos BOOLEAN NOT NULL,
        PRIMARY KEY (cpf)
        );'''

    cursor.execute(comando)

    # Efetivação do comando
    conexao.commit()

except conector.DatabaseError as err:
    print("Erro de banco de dados", err)

finally:
    # Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()

