import discord
from discord.ext import commands
import time
import json, ctypes
import time
import os, pystyle, random



os.system('pip uninstall --quiet discord -y')
os.system('pip uninstall --quiet discord.py -y')
os.system('pip install --quiet discord.py==1.7.3')
os.system('pip install --quiet pystyle')

settings = open("config.json")
config = json.load(settings)

min_delay = config["min_delay"]
max_delay = config["max_delay"]

os.system('cls')

try:
    ctypes.windll.kernel32.SetConsoleTitleW('Discord Clear DM | Made by ooxigen. | v1.0.0')
except Exception as e:
    print(e)

print(pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_purple, pystyle.Center.XCenter(f"""\n\n
░█████╗░░█████╗░██╗░░██╗██╗░██████╗░███████╗███╗░░██╗░░░  ░█████╗░██╗░░░░░███████╗░█████╗░██████╗░
██╔══██╗██╔══██╗╚██╗██╔╝██║██╔════╝░██╔════╝████╗░██║░░░  ██╔══██╗██║░░░░░██╔════╝██╔══██╗██╔══██╗
██║░░██║██║░░██║░╚███╔╝░██║██║░░██╗░█████╗░░██╔██╗██║░░░  ██║░░╚═╝██║░░░░░█████╗░░███████║██████╔╝
██║░░██║██║░░██║░██╔██╗░██║██║░░╚██╗██╔══╝░░██║╚████║░░░  ██║░░██╗██║░░░░░██╔══╝░░██╔══██║██╔══██╗
╚█████╔╝╚█████╔╝██╔╝╚██╗██║╚██████╔╝███████╗██║░╚███║██╗  ╚█████╔╝███████╗███████╗██║░░██║██║░░██║
░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝  ░╚════╝░╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝\n\n""")))

print(pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_purple, pystyle.Center.XCenter(f"""Version: v1.0.0""")))
print(pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_purple, pystyle.Center.XCenter(f"""Buy here: ooxigen.sellix.io\n\n\n""")))

bot = commands.Bot(command_prefix=config["prefix"], self_bot=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    print(pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_purple, pystyle.Center.XCenter(f"""[WELCOME] Account: {bot.user.name} ({bot.user.id})""")))
    print(pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_purple, pystyle.Center.XCenter(f"""[COMMAND] Use this command to perform cleanup: {config["prefix"]}clear\n\n\n\n\n""")))

@bot.command()
async def clear(ctx, limit: int=None):
    passed = 0
    failed = 0
    async for msg in ctx.message.channel.history(limit=limit):
        if msg.author.id == bot.user.id:
            try:
                time.sleep(random.randint(int(min_delay), int(max_delay)))
                await msg.delete()
                passed += 1
            except Exception as e:
                print(pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_purple, pystyle.Center.XCenter(e)))
                failed += 1
    print(pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_purple, pystyle.Center.XCenter(f"""Removed {passed} messages with {failed} fails""")))

bot.run(config["token"], bot=False)