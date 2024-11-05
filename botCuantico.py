import discord
import asyncio
from datetime import datetime
import json
import locale
from dotenv import load_dotenv
import os

# Inicializa el cliente del bot
intents = discord.Intents.default()
intents.message_content = True  # Asegúrate de habilitar el acceso a los mensajes
client = discord.Client(intents=intents)

load_dotenv()

# El token del bot (pon el tuyo aquí)
TOKEN = os.getenv("TOKEN")  # Reemplaza con tu token real

# ID del canal donde quieres enviar los recordatorios
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))  # Reemplaza con tu ID de canal


with open('recordatorios.json','r') as file:
  recordatorios = json.load(file)
#Lista de recordatorios (formato: {'fecha': 'YYYY-MM-DD', 'mensaje': 'Tu mensaje'})

# Comprueba si el contenido del mensaje es "hola, que día es"
async def enviar_recordatorios():
    await client.wait_until_ready()
    canal = client.get_channel(CHANNEL_ID)

    while not client.is_closed():
        # Obtiene la fecha actual
        fecha_actual = datetime.now().strftime('%Y-%m-%d')
        hora_actual = datetime.now().hour
        
        if 6 <= hora_actual <= 23:
            # Revisa si hay algún recordatorio para hoy
            for recordatorio in recordatorios:
                if recordatorio['fecha'] == fecha_actual:
                    # Envía el mensaje al canal
                    await canal.send(f"@everyone, {recordatorio['mensaje']}")

        # Espera seis horas para volver a comprobar 
        await asyncio.sleep(21600)

@client.event
async def on_ready():
    print(f'{client.user} esta ajustando los atomos')

    # Configura la actividad personalizada como "viendo videos"
    actividad = discord.Activity(type=discord.ActivityType.watching, name="atomos ser 1 y 0 a la vez")
    await client.change_presence(activity=actividad)

# Método recomendado en discord.py 2.x para inicialización de tareas asincrónicas
@client.event
async def setup_hook():
    # Crea una tarea para enviar los recordatorios
    asyncio.create_task(enviar_recordatorios())

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

@client.event
async def on_message(message):
    # Ignora los mensajes del propio bot
    if message.author == client.user:
        return
    
    if message.content.lower() == "Que tal tu cuenta de Steam?":
        try:
            await message.author.ban(reason="Las bromitas pesadas me tienen hasta el atomo")
        except discord.Forbidden:
            print("error permsisos")
        except discord.HTTPException:
            print("error conexion")

    if message.content.lower() == "que dia es?": 
        print("Pregunta recibida y mensaje enviado: Fecha")
        await message.channel.send(f"¡Hola {message.author.mention}! Hoy es {datetime.now().strftime('%A, %d de %B de %Y')}.")

    if message.content.lower() == "cuantos registros tengo?":
        print("Pregunta recibida y mensaje enviado: Registros")
        await message.channel.send(f"Recuerda {message.author.mention}, tenemos 32 registros de 64 bits.")

    if message.content.lower() == "como opero?":
        print("Pregunta recibida y mensaje enviado: Operacion")
        await message.channel.send(f"Aqui siempre operamos contraregistro, es importante que lo sepas {message.author.mention}.")

    if message.content.lower() == "hay magia?":
        print("Pregunta recibida y mensaje enviado: Magia")
        await message.channel.send(f"No {message.author.mention}, aqui nada sucede porque si, siempre hay un compoente que se encarga, y si no lo hace, pues ese componente no esta.")
    
    if message.content.lower() == "quien controla al sistema operativo?":
        print("Pregunta recibida y mensaje enviado: Sistema operativo")
        await message.channel.send(f"El sistema operativo es controlado por el propio sistema operativo,es asi {message.author.mention},es asi.")
    
    

# Ejecuta el bot
client.run(TOKEN)
