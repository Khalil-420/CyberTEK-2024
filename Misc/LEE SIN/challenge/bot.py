import discord
from discord.ext import commands
import sqlite3
import random

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

conn = sqlite3.connect('lee.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                  id INTEGER PRIMARY KEY,
                  username TEXT,
                  password TEXT
               )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS flags (
                  id INTEGER PRIMARY KEY,
                  flag TEXT
               )''')

cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('hackerman', 'supersecure'))
flag_name = "Securinets{i_see_all}"
cursor.execute('INSERT INTO flags (flag) VALUES (?)', (flag_name,))

conn.commit()

authenticated_members = set()

bot.remove_command('help')

def in_private_message(ctx):
    return isinstance(ctx.channel, discord.DMChannel)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
   if isinstance(message.channel, discord.DMChannel):
    if message.author == bot.user:
        return
    if not message.content.startswith('!'):
        quotes = [
            "My sight may be gone, but my vision holds true.",
            "Enlightenment is knowing the value of one's ignorance.",
            "The dragon must be unleashed, or it will consume me from within.",
            "The marks on my body are not warnings; they are reminders of the burden I bear.",
            "Enough blind jokes. Stop asking for more.",
            "I fail to see humor in that.",
            "The dragon sleeps, for now."
        ]
        random_quote = random.choice(quotes)
        await message.channel.send(random_quote)
    await bot.process_commands(message)

@bot.command(name='help')
async def custom_help(ctx):
    help_message = """
    *Custom Help Command*:```
 !auth password  (Authenticate with a password)
 !flag  (Display the flag)```
    """
    await ctx.send(help_message)

@bot.command(name='auth')
async def authenticate(ctx, *,password=None):
 try:
    if isinstance(ctx.channel, discord.DMChannel)==False:
        await ctx.send("I can't see here 👀 , DM me")
    elif " " in password : 
       await ctx.send("Passwords are without spaces, you forgot? 🤔")
    else:
     cursor.execute("SELECT username,id,password FROM users WHERE password ='" + password + "'")
     result = cursor.fetchone()
     print(result)
     if result:
        await ctx.send(f'Successfully Authenticated!')
        authenticated_members.add(ctx.author.id)
     else:
        print(f'{ctx.author} : {password}')
        await ctx.send('Authentication failed. Please try again.')
 except Exception:
     print(f'{ctx.author} : {password}')
     await ctx.send('Authentication failed. Please try again.')

@bot.command(name='flag')
async def check_flag(ctx):
    user_id = ctx.author.id
    if user_id in authenticated_members:
        if isinstance(ctx.channel, discord.DMChannel)==False:
           await ctx.send("I can't see here 👀 , DM me")
        if True:
           await ctx.send('Sorry :( the bot is under consturction but I\'m sure i kept the flag somewhere to save it for later')
    else:
        await ctx.send("You're not authenticated.")

bot.run('MTIxOTc0ODYyMDU4OTYwMDk3OA.G4s6NP.nn57fC1pIWOlW1iMkdxOiBGJmI08tFODVhfvO0')
