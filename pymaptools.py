'''
Copyright (c) 2022 Juan Carlos Bindez
This project is licensed under the MIT License.
'''


'''
Author: www.github.com/JuanBindez
Description: tools network
Python Version: 3.10
Local: Brazil
OS: Linux
'''


try:
    import os
    import time
    import webbrowser
    
    
    class Color():
        VERDE = '\033[92m'
        VERDE_CLARO = '\033[1;92m'
        VERMELHO = '\033[91m'
        AMARELO = '\033[93m'
        AZUL = '\033[1;34m'
        MAGENTA = '\033[1;35m'
        NEGRITO = '\033[;1m'
        CYANO = '\033[1;36m'
        CYANO_CLARO = '\033[1;96m'
        CINZA_CLARO = '\033[1;37m'
        CINZA_ESCURO = '\033[1;90m'
        PRETO = '\033[1;30m'
        BRANCO = '\033[1;97m'
        INVERTE = '\033[;7m'
        RESET = '\033[0m'


    def desenho_header():
        print(Color.VERMELHO +
            '''
                     ____        __  __           _____           _     
                    |  _ \ _   _|  \/  | __ _ _ _|_   _|__   ___ | |___ 
                    | |_) | | | | |\/| |/ _` | '_ \| |/ _ \ / _ \| / __|
                    |  __/| |_| | |  | | (_| | |_) | | (_) | (_) | \__ 
                    |_|    \__, |_|  |_|\__,_| .__/|_|\___/ \___/|_|___/ v 0.3
                           |___/             |_|
                           
                           
                           Copyright (c) 2022 Juan Carlos Bindez
    
            '''
        + Color.RESET)


    def install_tools(pacotes):
        print("seja Sudo!")
        os.system(pacotes)
        menu_header()


    def hosts_up():
        ip = str(input("ip >  "))
        os.system("nmap -sn -v {}".format(ip))
        menu_header()


    def docs_nmap():
        new = 2
        webbrowser.open("https://nmap.org/book/man-examples.html", new=new)
        menu_header()


    def minha_conexao():
        try:
            while 1 < 2:
                os.system("ifconfig")
                time.sleep(1)
                os.system("clear")
        except KeyboardInterrupt:
            os.system("clear")
            menu_header()
            
    def malware_scan():
        ip = str(input("ip >  "))
        os.system("nmap -v --script=malware {}".format(ip))
        menu_header()
        
        
    def tcp_udp_loop():
        while 1 < 2:
            try:
                time.sleep(2)
                os.system("netstat -tu")
                print("Concluido.")
                time.sleep(4)
                os.system("clear")
            except KeyboardInterrupt:
                os.system("clear")
                menu_header()
        

    def scan_deep():
        ip = str(input("ip >  "))
        print("####################### NMAP ###########################")
        os.system("sudo nmap -A -Pn -sS -v {}".format(ip))
        print("####################### WHOIS ###########################")
        os.system("whois {}".format(ip))
        menu_header()


    def menu_header():
        desenho_header()
        print(Color.AMARELO +
            
            '''
                          [ Ctrl + C ]  Para Encerrar o Programa
                          

                [1] Instalar As Ferramentas (root)  
                [2] Hosts Up                        
                [3] Scan Completo (Nmap, Whois)     [
                [4] Exemplos Nmap (site)
                [5] Minha Conexão
                [6] Scan Malware
                [7] Netstat (TCP/UDP)
            '''
        + Color.RESET)


        escolha = int(input(" > "))
        match escolha:

            case 1:
                install_tools('sudo apt install nmap')
                install_tools('sudo apt install whois')

            case 2:
                hosts_up()

            case 3:
                scan_deep()

            case 4:
                docs_nmap()

            case 5:
                minha_conexao()
                
            case 6:
                malware_scan()
                
            case 7:
                tcp_udp_loop()

            case _:
                print("digite apenas os numeros listados!")
            

    menu_header()
except KeyboardInterrupt:
    os.system("clear")
    desenho_header()
    print("Obrigado Por Usar O PyMapTools !")
