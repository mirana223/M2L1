import discord
import os
import random
from discord.ext import commands
from config import TOKEN

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
print(os.listdir('images'))

@bot.event
async def on_ready():
    print(f'we have logged in as {bot.user}')



@bot.command()
async def mem1(ctx):
    try:
        file_path = "images/mem1.png"
        with open(file_path,"rb") as f:
            picture = discord.File(f)
        await ctx.send(file=picture) 
    except:
        print("aranılan resme ulaşılamadı.") 

async def mem2(ctx):
    try:
        file_path = "images/mem2.png"
        with open(file_path,"rb") as f:
            picture = discord.File(f)
        await ctx.send(file=picture) 
    except:
        print("yok öyle bir şey. bun bulamadım.")
async def mem3(ctx):
    try:
        file_path = "images/mem3.png"
        with open(file_path,"rb") as f:
            picture = discord.File(f)
        await ctx.send(file=picture) 
    except:
        print("yok öyle bir şey. bun bulamadım.")
  




@bot.command()
async def mem_random(ctx):
    img_name = random.choice(os.listdir("images"))
    try:
    # Dosya adını bir değişkenden bu şekilde değiştirebilirsiniz!
        with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    except:
        print("aradığınız şeyi ben bilmem")


bot.run(TOKEN)        