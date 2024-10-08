import requests
from colorama import Fore
from urllib.request import urlopen 
from core import ui
import nmap
from nmap import PortScanner

def cep(cep):
    req = requests.get(f"https://viacep.com.br/ws/{cep}/json/").json()

    if req.items():
        for key, value in req.items():
            print(f'{Fore.RED}{key} == {value}')
    else:
        print(f"{Fore.RED}Nenhuma informação encontrada ou erro na consulta.")
    
    ui.question()

def cpf(cpf, base):
    if base == 1:
        url = f"https://centralbroxys.net/apis/cadsus/cpf.php?token=@BINGSIXBOT&cpf={cpf}"
    if base == 2:
        url = f"https://centralbroxys.net/apis/siregi/cpf.php?token=@BINGSIXBOT&cpf={cpf}"
    
    response = requests.get(url)

    if response.status_code == 200:
        if base == 1:
            return response.json()
        if base == 2:
            return response.json()['dados']
    else:
        return None  # Nenhuma informação encontrada ou erro na consulta

def nmap():
    ui.menu_nmap()
    resposta3 = int(input('O que deseja fazer? \n⤷  '))
    if resposta3 == 1:
        os.environ['PATH'] += r"/usr/bin/nmap"
        nm = PortScanner(input("Digite o IP \n ⤷"))
        print(nm.scaninfo())
    
def pergunta():
    resposta1 = int(input('O que você deseja fazer? \n⤷  '))
    if resposta1 == 1:
        try:
            Ip()
        except Exception as  ex:
            print(f"{Fore.RED}Error: ({ex})")
    if resposta1 == 2:
        nmap()
    
def Ip():
    ip = input(f'{Fore.WHITE}Digite o IP\n⤷  ')
    
    if ip: 
        url = f"http://ip-api.com/json/{ip}"

        request = urlopen(url)
        data = request.read().decode()

        data = eval(data)

        for i in data:
            print(f"{Fore.RED}{i} == {data[i]}")
        
        ui.question()
    else:
        return None
