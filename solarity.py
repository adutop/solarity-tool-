import os
import random
import colorama
from colorama import Fore
import discord.ext
import discord
from colorama import init, Fore, Back, Style
import socket 
from os import system, name
from time import sleep
import requests
import json
import random, string
import string
from discord_webhooks import DiscordWebhooks
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')  
init(convert=True)
##logo 
logo = ((f"""  {Fore.WHITE}    ┌─┐┌─┐┬  ┌─┐┬─┐┬┌┬┐┬ ┬
{Fore.CYAN}      └─┐│ ││  ├─┤├┬┘│ │ └┬┘
{Fore.WHITE}      └─┘└─┘┴─┘┴ ┴┴└─┴ ┴  ┴
   {Fore.RED}[{Fore.WHITE}https://dsc.gg/{Fore.GREEN}optimized{Fore.RED}]"""))




##login 
print(logo)
print(f"{Fore.RED}╔{Fore.WHITE}solarity{Fore.YELLOW}@{Fore.CYAN}username")
user_name = input(f"╚═══")
if user_name == "root":
    print(f"{Fore.RED}╔{Fore.WHITE}solarity{Fore.YELLOW}@{Fore.CYAN}password")
passw = input(f"╚═══")
if passw == "root":
    
    screen_clear()
    print(f"    {Fore.WHITE}-{Fore.GREEN}Welcome {Fore.WHITE}{socket.gethostname()}{Fore.WHITE}-")
    sleep(2)
    screen_clear()
    print(logo)
    print(f"   {Fore.RED}Type {Fore.WHITE} ? {Fore.RED} for command list    ")
    print(f"{Fore.RED}╔{Fore.WHITE}solarity{Fore.YELLOW}@{Fore.CYAN}{socket.gethostname()}")
    main_in = input(f"╚═══")
    print(f'{Fore.RED}╚═{Fore.WHITE}solarity{Fore.YELLOW}@{Fore.CYAN}Amount{Fore.WHITE}[>]')

    if main_in == "?":
      screen_clear()
      print(f"     {Fore.CYAN}╔═════════════════════════════════{Fore.MAGENTA}══╗")
      print(f"     {Fore.CYAN}║ {Fore.WHITE}Webhook Spammer                   {Fore.MAGENTA}║")
      print(f"     {Fore.CYAN}║ {Fore.WHITE}Nitro Gen                        {Fore.MAGENTA} ║")
      print(f"     {Fore.CYAN}║                                  {Fore.MAGENTA} ║")
      print(f"     {Fore.MAGENTA}║                                  {Fore.MAGENTA} ║")
      print(f"     {Fore.MAGENTA}╚═══════════════════════════════════╝")
    print(f"{Fore.RED}╔{Fore.WHITE}solarity{Fore.YELLOW}@{Fore.CYAN}{socket.gethostname()}")
    main_in = input(f"╚═══")



#if main_in == "webhook":
      #webhook_url = input(f"{Fore.RED}╚═{Fore.WHITE}solarity{Fore.YELLOW}@{Fore.CYAN}URL{Fore.WHITE}[>] ")
      #message = input(f'{Fore.RED}╚═{Fore.WHITE}solarity{Fore.YELLOW}@{Fore.CYAN}Message{Fore.WHITE}[>]')
      #ilosc = int(input(f'{Fore.RED}╚═{Fore.WHITE}solarity{Fore.YELLOW}@{Fore.CYAN}Amount{Fore.WHITE}[>]'))
      
#webhook = DiscordWebhooks(webhook_url)
#webhook.set_content(title=message
                    #description='Spammed by solarity multi tool [https://dsc.gg/optimized]'
                    #color=0xF58CBA)
#for i in range(ilosc):
    #webhook.send()


if main_in == "nitro":
   print(f"{Fore.RED}╔{Fore.WHITE}solarity{Fore.YELLOW}@{Fore.CYAN}{socket.gethostname()}{Fore.WHITE}NITROGEN")
   amount = int(input(f'{Fore.RED}╚═{Fore.WHITE}solarity{Fore.YELLOW}@{Fore.CYAN}AMOUNT{Fore.WHITE}[>]')) 
   value = 1
   while value <= amount:
       code = "https://discord.gift/" + ('').join(random.choice(string.anscii_letters + string.digits, k=16))
       f = open('Nitro.txt', "a+")
       f.write(f'{code}\n')
       f.close
       print(f'{Fore.RED}╚═{Fore.WHITE}solarity{Fore.YELLOW}@{Fore.CYAN}GENERATED{Fore.WHITE}[>] {code}')
       value += 1
   
      



