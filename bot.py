import discord 
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content=True

EcoBot= commands.Bot(command_prefix="/",intents=intents)

@EcoBot.event
async def on_ready():
    print(f"Se ha iniciado como {EcoBot.user}")


ideas=["1. Crear una maceta con una botella de plástico", "2. Convertir una caja de cartón en una casa para pájaros","3. Hacer decoraciones de Pascua, de Halloween, de Navidad o de lo que sea"]

reciclables=["botella de plástico", "icopor", "papel", "cartón", "aluminio", "papel", "vidrio", "latas", "baterias", "ropa"]
basura=["pañales", "hisopos", "jeringas"]


@EcoBot.command()
async def manualidades(ctx):
    await ctx.send(random.choice(ideas))

@EcoBot.command()
async def clasificar(ctx,*,objeto:str):
    if objeto in reciclables:
        await ctx.send(f"El objeto {objeto} es reciclable")
    elif objeto in basura:
        await ctx.send("El objeto es basura")
    else:
        await ctx.send("Aún no he sido programado para clasificar el objeto que me dijiste")
