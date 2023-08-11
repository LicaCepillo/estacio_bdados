import sqlite3 as conector

# Abertura de conexão e aquisição de curso
conexao = conector.connect ('lilian_atividades/banco_dados_exemplo2.db')
cursor = conexao.cursor()

# Execução de um comando: SELECT / CREATE
comando = '''CREATE TABLE Veiculo (
            placa CHARACTER(7) NOT NULL,
            ano INTEGER NOT NULL,
            cor TEXT NOT NULL,
            proprietario INTEGER NOT NULL,
            marca INTEGER NOT NULL, 
            PRIMARY KEY (placa),
            FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
            FOREIGN KEY(marca) REFERENCES Marca(id)
);'''

cursor.execute(comando)

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()