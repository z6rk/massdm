
import discord
from discord.ext import commands
import colorama 
import os
from colorama import Fore
client = commands.Bot(command_prefix = 'a niglet', help_command = None)
# xc loves you

colorama.init()
token = input("Type Your Token>>")
@client.event
async def on_ready():
 os.system('cls')
 print(f'''  
{Fore.MAGENTA}       ███████╗████████╗███████╗██████╗░███╗░░██╗██╗████████╗██╗░░░██╗
{Fore.MAGENTA}       ██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗░██║██║╚══██╔══╝╚██╗░██╔╝
{Fore.MAGENTA}       █████╗░░░░░██║░░░█████╗░░██████╔╝██╔██╗██║██║░░░██║░░░░╚████╔╝░
{Fore.MAGENTA}       ██╔══╝░░░░░██║░░░██╔══╝░░██╔══██╗██║╚████║██║░░░██║░░░░░╚██╔╝░░
{Fore.MAGENTA}       ███████╗░░░██║░░░███████╗██║░░██║██║░╚███║██║░░░██║░░░░░░██║░░░
{Fore.MAGENTA}       ╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░░╚═╝░░░░░░╚═╝░░░
{Fore.MAGENTA}       _______________________________________________________________
{Fore.MAGENTA}                  By xc#1500              
{Fore.MAGENTA}                      [1] Mass Dm                                               
''')
 fuck = input(f"{Fore.CYAN}Select>>")
 if fuck == '1':
  input2 = input(f"{Fore.GREEN}What Should I Send??>>")
  for user in client.user.friends:                
   await user.send(f"{input2}")
   print(f"{Fore.GREEN}[+] Sent{Fore.WHITE} {input2} To {user}")

client.run(token, bot = False) 
