#PyTyper
#A hackertyper knockoff by j4y_boi
#https://github.com/j4y-boi/pytyper

import random
import sys
from time import sleep as wait
import readchar
import os

typedSnippets = 0
leaving = False
typedcode = ""
oldx = 0
oldy = 0

TerminalCol = 62
TerminalLin = 12

splashscreenText = [
    "hacking = True",
    "s0 3p1k h4x0r",
    "Accessing mainframe...",
    "404, didn't find text",
    "*keyboard noises*",
    "gotta love Hollywood",
    "bypassing the firewall??? :0",
]

snipppets = [ # i ai generated most of these... sorry :c
    "---------\nimport os\nimport sys",
    "def hack_the_planet():\n    print('Accessing mainframe...')",
    "class Exploit:\n    def __init__(self, target):\n        self.target = target\n    def attack(self):\n        print(f'Pinging {self.target}...')",
    "def brute_force(password):\n    for attempt in range(10000):\n        if attempt == password:\n            return 'Access Granted'",
    "def encrypt_data(data):\n    return ''.join(chr(ord(c) ^ 42) for c in data)  # Totally unbreakable XOR cipher",
    "def backdoor():\n    print('Listening on port 1337...')\n    return 'Access key: 0xDEADBEEF'",
    "class Virus:\n    def __init__(self):\n        self.payload = 'Just a prank, bro!'\n    def execute(self):\n        print(self.payload)",
    "def spoof_ip():\n    return '192.168.1.' + str(random.randint(2, 254))  # Untraceable!'",
    "def deep_web_access():\n    print('Booting Tor nodes...')\n    return 'Welcome to the shadows.'",
    "def bypass_firewall():\n    print('Tunneling through port 443...')\n    return 'Packet disguised as HTTPS traffic'",
    "class QuantumHack:\n    def __init__(self, qubits=4):\n        self.qubits = qubits\n    def compute(self):\n        print(f'Cracking encryption with {self.qubits} qubits...')",
    "import socket\nimport struct\nprint('Socket module initialized')",
    "def inject_sql():\n    query = \"SELECT * FROM users WHERE name = 'admin' --'\"\n    print(f'Executing: {query}')",
    "def scramble_logs():\n    print('Erasing syslogs and access records...')\n    return 'Logs scrambled successfully'",
    "def fake_identity():\n    return f'User-Agent: {random.choice([\"Mozilla/5.0\", \"curl/7.68.0\", \"Nmap Scripting Engine\"])}/Python'",
    "class ZeroDay:\n    def __init__(self, target):\n        self.target = target\n    def deploy(self):\n        print(f'Exploiting unknown vulnerability on {self.target}...')",
    "def create_botnet():\n    print('Connecting to zombie nodes...')\n    return f'Botnet online. Nodes: {random.randint(1000, 5000)}'",
    "def decrypt_data(data, key):\n    return ''.join(chr(ord(c) ^ key) for c in data)  # 1337-level encryption",
    "def evade_heuristics():\n    print('Obfuscating payload and polymorphing...')\n    return 'Signature undetected!'",
    "class Darknet:\n    def __init__(self):\n        self.market = 'Fabricroute 3.0'\n    def access(self):\n        print(f'Browsing {self.market}...')",
    "def reverse_shell():\n    print('Opening reverse shell on port 4444...')\n    return 'Connected to remote host.'",
    "class AI_Hacker:\n    def __init__(self):\n        self.model = 'GPT-1337'\n    def generate_exploit(self):\n        return 'Generating next-gen cyberattack...' ",
]

def printBox(lenv:int,*sentences:str):
    length = lenv
    lines = []

    for sentence in sentences:
        split_lines = sentence.split("\n")
        lines.extend(split_lines)

    for i in lines:
        if len(i) > length:
            length = len(i)

    print(f"┌{"─"*length}┐")
    for r in lines:
        print(f"│{r.center(length)}│")
    print(f"└{"─"*length}┘")

def clearterminal(header:bool): #compatibility, am i right
    os.system("cls" if os.name == "nt" else "clear")
    sys.stdout.write("\033[32m")
    if header:
        printBox(60,"[H A C K I N G   T E R M I N A L]",f"-\n{chosenSplashscreen}")

def hacker_typer():
    global leaving
    global typedSnippets
    global typedcode

    code = random.choice(snipppets)
    index = 0

    while index < len(code):
        key = readchar.readkey()
        if key == '\x1b':  # esc for exit
            clearterminal(False)
            print("[ See ya next time :) ]")
            leaving = True
            break
        if os.get_terminal_size().columns < TerminalCol or os.get_terminal_size().lines < TerminalLin:
            break  # terminal too small
        sys.stdout.write(code[index])
        typedcode = typedcode + code[index]
        sys.stdout.flush()
        index += 1
        #wait(0.01)

    if not leaving:
        sys.stdout.write("\n\n")
        typedcode = typedcode + "\n\n"

    typedSnippets += 1

chosenSplashscreen = splashscreenText[random.randint(0,len(splashscreenText)-1)]

if __name__ == "__main__":
    clearterminal(False)
    printBox(60,"▀█▀ █▄█ █▀█ █▀▀ █▀█ █▀█ █▄█\n █   █  █▀▀ ██▄ █▀▄ █▀▀  █ \nA hackertyper knockoff by j4y_boi","-","[Press any key to type, press 'ESC' to exit.]","(Go in fullscreen for the FULL experience.)","Press any key to begin.")
    key = readchar.readkey()
    clearterminal(True)
    leaving = False
    while not leaving:
        term_x, term_y = os.get_terminal_size().columns, os.get_terminal_size().lines

        if term_x < TerminalCol or term_y < TerminalLin:
            while term_x < TerminalCol or term_y < TerminalLin:
                newx, newy = os.get_terminal_size().columns, os.get_terminal_size().lines
                
                if newx != oldx or newy != oldy:
                    oldx, oldy = newx, newy
                    clearterminal(False)
                    print("\n" * (newy // 2 - 1))  # Centering
                    print("Your terminal is too small!".center(newx))
                
                wait(0.5)  # Avoid overloading the CPU with constant checking
                term_x, term_y = os.get_terminal_size().columns, os.get_terminal_size().lines

            clearterminal(True)
            print(typedcode)
        else:
            hacker_typer()

            if typedSnippets % 10 == 0 and typedSnippets != 0:
                clearterminal(True)
                printBox(60, "Processing packets...")
                wait(5)
                for i in range(6):
                    clearterminal(True)
                    if i % 2 == 0:
                        printBox(60, f"Processed units: {typedSnippets}")
                    else:
                        printBox(60, "")
                    wait(1)
                clearterminal(True)
                printBox(60, "Continuing...")
                wait(5)
                clearterminal(True)
                print(typedcode)
            elif random.randint(1,1) == 1:
                printBox(60, "Bypassing passcode...")
                wait(5)
                choice = random.randint(1,3)
                if choice == 1:
                    for i in range(6):
                        clearterminal(True)
                        print("\033[31m",end="")
                        if i % 2 == 0:
                            printBox(60, "Access Denied")
                        else:
                            printBox(60, "")
                        wait(1)
                elif choice == 2:
                    for i in range(6):
                        clearterminal(True)
                        if i % 2 == 0:
                            printBox(60, f"Access Granted")
                        else:
                            printBox(60, "")
                        wait(1)
                else:
                    for i in range(6):
                        clearterminal(True)
                        print("\033[33m",end="")
                        if i % 2 == 0:
                            printBox(60, "ERROR: COULDN'T RESOLVE PASS_BYPASS")
                        else:
                            printBox(60, "")
                        wait(1)
                        
                clearterminal(True)
                printBox(60, "Continuing...")
                wait(5)
                clearterminal(True)
                print(typedcode)
            elif random.randint(1,20) == 1:
                printBox(60, "Resolving hash...")
                wait(5)
                choice = random.randint(1,3)
                if choice == 1:
                    for i in range(6):
                        clearterminal(True)
                        print("\033[31m",end="")
                        if i % 2 == 0:
                            printBox(60, "FAILED: INSUFFICIENT RESOURCES")
                        else:
                            printBox(60, "")
                        wait(1)
                elif choice == 2:
                    for i in range(6):
                        clearterminal(True)
                        if i % 2 == 0:
                            printBox(60, f"Success!")
                        else:
                            printBox(60, "")
                        wait(1)
                else:
                    for i in range(6):
                        clearterminal(True)
                        print("\033[33m",end="")
                        if i % 2 == 0:
                            printBox(60, "ERROR: ERROR WHILE RESOLVING")
                        else:
                            printBox(60, "")
                        wait(1)

                clearterminal(True)
                printBox(60, "Continuing...")
                wait(5)
                clearterminal(True)
                print(typedcode)
