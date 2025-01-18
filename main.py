import os, requests
import discord
import random
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def lista(ctx):
    await ctx.send(f"Comandos: manualidad_botella, manualidad_rollo_papel, manualidad_pitillo carton_huevos")

@bot.command()
async def manualidad_botella(ctx):
    await ctx.send(f"Manualidad con botellas: https://www.youtube.com/watch?v=75B8pGCk4Y4")

@bot.command()
async def manualidad_rollo_papel(ctx):
    await ctx.send(f"Manualidad con un rollo de papel: https://www.youtube.com/watch?v=JSFyODoaXWM")

@bot.command()
async def manualidad_pitillo(ctx):
    await ctx.send(f"Manualidad con pitillos: https://www.youtube.com/watch?v=KSIJE0K0cb4")

@bot.command()
async def carton_huevos(ctx):
    await ctx.send(f"Manualidad con cartones de huevos: https://www.youtube.com/watch?v=GeKmhaXz-94")
