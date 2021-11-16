import sqlite3
from sqlite3 import Error

conn = sqlite3.connect('banco_cad.bd')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS cadastro (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    login TEXT NOT NULL,
    senha TEXT NOT NULL,
    nivel INTEGER NOT NULL 
);
""")#cria o banco de dados do programa, caso ja tenha a tabela este comando é ignorado.