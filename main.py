# SHELBY CLONER
from os import system
import psutil
from pypresence import Presence
import time
import sys
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from hackersop import shelby
# MUST JOIN .gg/hackersop
client = discord.Client(intents=discord.Intents.default())
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.YELLOW}
                                   
██╗░░██╗░█████╗░  ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
██║░░██║██╔══██╗  ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
███████║██║░░╚═╝  ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██████╔╝
██╔══██║██║░░██╗  ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██╔══██╗
██║░░██║╚█████╔╝  ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██║░░██║
╚═╝░░╚═╝░╚════╝░  ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
=========================== HC =====================================
              MADE BY SHELBY | Join .gg/hackersop
=========================== HC =====================================
{Style.RESET_ALL}
                                                            {Fore.MAGENTA}{Style.RESET_ALL}
        """)
token = input(Fore.RED + '(HC CLONER) Token:\n >')
guild_s = input('Please enter guild id you want to copy:\n >')
guild = input('Please enter guild id where you want to copy:\n >')
input_guild_id = guild_s
output_guild_id = guild
token = token

# SKIDERSSS KI MKB

print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"Logged In as : {client.user}")
    print("Cloning Server")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await shelby.guild_edit(guild_to, guild_from)
    await shelby.roles_delete(guild_to)
    await shelby.channels_delete(guild_to)
    await shelby.roles_create(guild_to, guild_from)
    await shelby.categories_create(guild_to, guild_from)
    await shelby.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}
    CLONED ! 
    MUST JOIN .gg/hackersop
    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    client.close()


client.run(token, bot=False)
