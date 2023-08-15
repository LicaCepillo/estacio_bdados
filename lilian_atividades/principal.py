import sqlite3 as conector
from modelo import Municipio, Dengue

  
conexao = None
cursor = None

try:
    
    conexao = conector.connect('lilian_atividades/meu_banco.db')
    cursor = conexao.cursor()

    with open("lilian_atividades/dengue_2018rj.csv") as arquivo:
        arquivo.readline () #descarta o cabeçalho
        for linha in arquivo:
            codigo, nome, casos_2018, casos_2019 = linha.strip().split(',')
            print(codigo, nome, casos_2018, casos_2019)

        municipio = Municipio (codigo, nome)
        comando= '''INSERT INTO Municipio VALUES (:codigo,:nome);''' # parâmetros nomeados
        
        cursor.execute(comando, vars(municipio))
        dengue_2018 = Dengue (codigo, 2018, int(casos_2018))
        dengue_2019 = Dengue (codigo, 2019, int(casos_2019))

        comando= '''INSERT INTO Dengue VALUES (:codigo, :ano, :casos);''' # parâmetros nomeados
        cursor.execute(comando, vars(dengue_2018))
        cursor.execute(comando, vars(dengue_2019))

    with open("lilian_atividades/populacao.csv") as arquivo:
        arquivo.readline() #descarta o cabeçalho
        for linha in arquivo2:
            codigo, nome, pop_2018, pop_2019 = linha.strip().split(',')
            print(codigo, nome, pop_2018, pop_2019)
            comando = '''INSERT INTO Populacao VALUES (?,?,?);''' #delimitador ?
            cursor.execute(comando, (codigo, 2018, pop_2018))
            cursor.execute(comando, (codigo, 2019, pop_2018))
    
    conexao.commit()

except conector.OperationalError as erro:
    print("Erro Operacional", erro)
except conector.DatabaseError as erro:
    print("Erro de Banco de Dados", erro)
