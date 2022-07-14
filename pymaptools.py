'''
"This project is licensed under the MIT License."
Author: www.github.com/JuanBindez
License: https://github.com/JuanBindez/PyMapTools/blob/main/LICENSE
Description: tools network
Python Version: 3.10
year: 2022
Local: Brazil
OS: Linux
'''

try:
    import os
    import time
    import webbrowser


    def desenho_header():
        print(
            '''
                     ____        __  __           _____           _     
                    |  _ \ _   _|  \/  | __ _ _ _|_   _|__   ___ | |___ 
                    | |_) | | | | |\/| |/ _` | '_ \| |/ _ \ / _ \| / __|
                    |  __/| |_| | |  | | (_| | |_) | | (_) | (_) | \__ 
                    |_|    \__, |_|  |_|\__,_| .__/|_|\___/ \___/|_|___/
                            |___/             |_|           
    
            '''
        )


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



    def scan_deep():
        ip = str(input("ip >  "))
        print("####################### NMAP ###########################")
        os.system("nmap -A -Pn -v {}".format(ip))
        print("####################### WHOIS ###########################")
        os.system("whois {}".format(ip))
        print("####################### MTR ###########################")
        os.system("mtr {}".format(ip))
        menu_header()


    def menu_header():
        desenho_header()
        print(
            
            '''
                          [ Ctrl + C ]  Para Encerrar o Programa

                          

                [1] Instalar As Ferramentas (root)  [5] Minha Conexão
                [2] Hosts Up
                [3] Scan Profundo
                [4] Exemplos Nmap
            '''
        )


        escolha = int(input(" > "))
        match escolha:

            case 1:
                install_tools('apt install nmap')
                install_tools('apt install whois')
                install_tools('apt install mtr')

            case 2:
                hosts_up()

            case 3:
                scan_deep()

            case 4:
                docs_nmap()

            case 5:
                minha_conexao()

            case _:
                print("digite apenas os numeros listados!")
            

    menu_header()
except KeyboardInterrupt:
    os.system("clear")
    desenho_header()
    print("Obrigado Por Usar O PyMapTools !")
