import sqlite3 as conector
from modelo import Municipio, Dengue

  
conexao = None
cursor = None

try:
    
    conexao = conector.connect('lilian_atividades/meu_banco.db')
    cursor = conexao.cursor()

    with open("lilian_atividades/populacao.csv") as arquivo:
        arquivo.readline() #descarta o cabeçalho
        for linha in arquivo:
            codigo, nome, pop_2018, pop_2019 = linha.strip().split(',')
            print(codigo, nome, pop_2018, pop_2019)
            
            comando = '''INSERT INTO Populacao VALUES (?,?,?);''' #delimitador ?
            cursor.execute(comando, (codigo,2018, pop_2018))
            cursor.execute(comando, (codigo,2019,pop_2019))
    conexao.commit()

except conector.OperationalError as erro:
    print("Erro Operacional", erro)
except conector.DatabaseError as erro:
    print("Erro de Banco de Dados", erro)
