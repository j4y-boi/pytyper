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

splashscreenText = [
    "hacking = True",
    "s0 3p1k h4x0r",
    "Accessing mainframe...",
    "404, didn't find text",
    "*keyboard noises*",
    "gotta love Hollywood"
]

snipppets = [ # i ai generated some of these... sorry :c
    "---------\nimport os\nimport sys",
    "def hack_the_planet():\n    print('Accessing mainframe...')",
    "class Exploit:\n    def __init__(self, target):\n        self.target = target\n    def attack(self):\n        print(f'Pinging {self.target}...')",
    "def brute_force(password):\n    for attempt in range(10000):\n        if attempt == password:\n            return 'Access Granted'"
    "def encrypt_data(data):\n    return ''.join(chr(ord(c) ^ 42) for c in data)  # Totally unbreakable XOR cipher",
    "def backdoor():\n    print('Listening on port 1337...')\n    return 'Access key: 0xDEADBEEF'",
    "class Virus:\n    def __init__(self):\n        self.payload = 'Just a prank, bro!'\n    def execute(self):\n        print(self.payload)",
    "def spoof_ip():\n    return '192.168.1.' + str(random.randint(2, 254))  # Untraceable!'",
    "def deep_web_access():\n    print('Booting Tor nodes...')\n    return 'Welcome to the shadows.'",
    "def bypass_firewall():\n    print('Tunneling through port 443...')\n    return 'Packet disguised as HTTPS traffic'",
    "class QuantumHack:\n    def __init__(self, qubits=4):\n        self.qubits = qubits\n    def compute(self):\n        print(f'Cracking encryption with {self.qubits} qubits...')",
    "def hack() #does quite everything\n    hack = True #because that's how it works apparently\n   print(hack.status)"
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

def clearterminal(): #compatibility, am i right
    os.system("cls" if os.name == "nt" else "clear")
    sys.stdout.write("\033[32m")

def hacker_typer():
    global leaving
    global typedSnippets

    code = random.choice(snipppets)
    index = 0

    while index < len(code):
        key = readchar.readkey()
        if key == '\x1b':  # esc for exit
            clearterminal()
            print("[ See ya next time :) ]")
            leaving = True
            break
        sys.stdout.write(code[index])
        sys.stdout.flush()
        index += 1
        wait(0.02)

    sys.stdout.write("\n")

    typedSnippets += 1

chosenSplashscreen = splashscreenText[random.randint(0,len(splashscreenText)-1)]

if __name__ == "__main__":
    clearterminal()
    printBox(60,"▀█▀ █▄█ █▀█ █▀▀ █▀█ █▀█ █▄█\n █   █  █▀▀ ██▄ █▀▄ █▀▀  █ \n","[Press any key to type, press 'ESC' to exit.]","(Go in fullscreen for the FULL experience.)","Press any key to begin")
    key = readchar.readkey()
    clearterminal()
    printBox(60,"[H A C K I N G   T E R M I N A L]",chosenSplashscreen)
    leaving = False
    while leaving == False:
        hacker_typer()
        if typedSnippets % 10 == 0 and not typedSnippets == 0:
            clearterminal()
            printBox(60,"[H A C K I N G   T E R M I N A L]",chosenSplashscreen)
            printBox(60,"Processing packets...")
            wait(5)
            for i in range(6):
                clearterminal()
                printBox(60,"[H A C K I N G   T E R M I N A L]",chosenSplashscreen)
                if i%2 == 0:
                    printBox(60,f"Processed units: {typedSnippets}")
                else:
                    printBox(60,"")
                wait(1)
            clearterminal()
            printBox(60,"[H A C K I N G   T E R M I N A L]",chosenSplashscreen)
            printBox(60,"Continuing...")
            wait(5)
            clearterminal()
            printBox(60,"[H A C K I N G   T E R M I N A L]",chosenSplashscreen)
