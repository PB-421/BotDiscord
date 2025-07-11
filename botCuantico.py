import discord
import asyncio
import random
from datetime import datetime
import json
import locale
from discord.ext import commands
from dotenv import load_dotenv
import os

# Inicializa el cliente del bot con comandos
intents = discord.Intents.default()
intents.message_content = True  # Habilitar acceso a los mensajes
bot = commands.Bot(command_prefix="/", intents=intents)

load_dotenv()

# El token del bot (pon el tuyo aquí)
TOKEN = os.getenv("TOKEN")  # Reemplaza con tu token real

# ID del canal donde quieres enviar los recordatorios
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))  # Reemplaza con tu ID de canal


with open('recordatorios.json','r') as file:
  recordatorios = json.load(file)
# Carga la lista de recordatorios

with open('frases.json','r') as file2:
  frases_random = json.load(file2)
# Carga la lista de frases    

async def enviar_recordatorios():
    await bot.wait_until_ready()
    canal = bot.get_channel(CHANNEL_ID)
    if not canal:
        print("No se encontró el canal, id invalido.")
        return

    while not bot.is_closed():
        fecha_actual = datetime.now().strftime('%Y-%m-%d')
        hora_actual = datetime.now().hour
        minuto_actual = datetime.now().minute
        sent = False

        if (hora_actual == 9 or hora_actual == 15 or hora_actual == 22) and minuto_actual == 0:
                for recordatorio in recordatorios:
                    if recordatorio['fecha'] == fecha_actual:
                        await canal.send(f"@everyone, {recordatorio['mensaje']}")
                        sent = True
                if (sent):
                    await asyncio.sleep(60)
            
        await asyncio.sleep(5)  # Espera 5 segundos para volver a comprobar


@bot.event
async def on_ready():
    # Sincroniza los comandos y configura la presencia del bot
    await bot.tree.sync()
    print(f'{bot.user} está ajustando los átomos')
    
    actividad = discord.Activity(type=discord.ActivityType.watching, name="átomos ser 1 y 0 a la vez")
    await bot.change_presence(activity=actividad)
    
    # Inicia la tarea enviar_recordatorios una vez que el bot esté listo
    asyncio.create_task(enviar_recordatorios())

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

# Configura los comandos de barra con app_commands
@bot.tree.command(name="que_dia_es", description="Que día es hoy?")
async def que_dia_es(interaction: discord.Interaction):
    await interaction.response.send_message(f"¡Hola {interaction.user.mention}! Hoy es {datetime.now().strftime('%A, %d de %B de %Y')}.")

@bot.tree.command(name="cuantos_registros_tengo", description="Este numero es importante")
async def cuantos_registros_tengo(interaction: discord.Interaction):
    await interaction.response.send_message(f"Recuerda {interaction.user.mention}, tenemos 32 registros de 64 bits.")

@bot.tree.command(name="como_opero", description="Es bueno saber como operas")
async def como_opero(interaction: discord.Interaction):
    await interaction.response.send_message(f"Aquí siempre operamos contraregistro, es importante que lo sepas {interaction.user.mention}.")

@bot.tree.command(name="hay_magia", description="Las cosas funcionan con magia?")
async def hay_magia(interaction: discord.Interaction):
    await interaction.response.send_message(f"No {interaction.user.mention}, aquí nada sucede porque sí, siempre hay un componente que se encarga, y si no lo hace, pues ese componente no está.")

@bot.tree.command(name="quien_controla_sistema_operativo", description="Quien le protege?")
async def quien_controla_sistema_operativo(interaction: discord.Interaction):
    await interaction.response.send_message(f"El sistema operativo es controlado por el propio sistema operativo, es así {interaction.user.mention}, es así.")

@bot.tree.command(name="tomasulo", description="Quien es tomasulo??")
async def tomasulo(interaction: discord.Interaction):
    await interaction.response.send_message(f"El que te mete el pirulo....")

@bot.tree.command(name="raul", description="Si")
async def raul(interaction: discord.Interaction):
    respuesta = random.choice(frases_random)
    await interaction.response.send_message(respuesta)

# Ejecuta el bot
bot.run(TOKEN)