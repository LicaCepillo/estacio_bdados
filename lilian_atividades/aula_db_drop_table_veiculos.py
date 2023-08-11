import sqlite3 as conector

# Abertura de conexão e aquisição de um cursor
conexao = conector.connect('lilian_atividades/banco_dados_exemplo2.db')
cursor = conexao.cursor()

# Execução de um comando DROP TABLE
comando1 = '''DROP TABLE Veiculo;'''

cursor.execute(comando1)

comando2 = '''CREATE TABLE Veiculo (
                placa CHARACTER(7) NOT NULL,
                ano INTEGER NOT NULL,
                cor TEXT NOT NULL,
                motor REAL NOT NULL,
                proprietario INTEGER NOT NULL,
                marca INTEGER NOT NULL,
                PRIMARY KEY (placa),
                FOREIGN KEy (proprietario) REFERENCES pessoa(cpf),
                FOREIGN KEY (marca) REFEFRNCES Marca(id)
            );'''

cursor.execute(comando2)

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()