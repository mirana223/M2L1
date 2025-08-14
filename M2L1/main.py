import discord
import os
import random
from discord.ext import commands
from config import TOKEN
from visualanalys import mems
from visualanalys import all_mems
from duck import *
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
help_list = ["mem_show: Memleri gösterir.", "rand_mem: Memlerden rastgele birini gösterir.",
             "duck: Random bir ördek resmi gönderir.", "dog: Random bir köpek resmi gönderir.",
             "fox: Random bir tilki resmi gönderir.", "pokemon: Random bir pokemon resmi gönderir.",
             "mem_yazilim: Rastgele bir mem resmi gönderir."
]
@bot.event
async def on_ready():
    print(f'we have logged in as {bot.user}')
@bot.command()
async def mem_show(ctx):
    await mems(ctx)

@bot.command()
async def rand_mem(ctx):
    await all_mems(ctx)

@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
@bot.command()
async def dog(ctx):
    image_url = get_dog_image_url
    await ctx.send(image_url)

@bot.command()
async def fox(ctx):
    image_url = get_fox_image_url
    await ctx.send(image_url)

@bot.command()
async def pokemon(ctx):
    # Burada get_pok_image_url fonksiyonunu çağırıyoruz.
    # Ancak fonksiyonun içeriği hatalı, düzeltmemiz gerekiyor.
    # Düzgün bir URL döndürmesi için fonksiyonu güncelleyermemiz lazım.
    # Şu anki haliyle fonksiyon düzgün çalışmayacak.
    # Aşağıdaki kodu düzeltmek için get_pok_image_url fonksiyonunu güncellemeliyiz.
    # Örnek olarak, PokeAPI'den rast
    image_url = get_pok_image_url
    await ctx.send(image_url)
            

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
async def mem_yazilim(ctx):
    img_name = random.choice(os.listdir("images"))
    help_list.append("mem_yazilim: Rastgele bir mem resmi gönderir.")
    try:
    # Dosya adını bir değişkenden bu şekilde değiştirebilirsiniz!
        with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    except:
        print("aradığınız şeyi ben bilmem")
@bot.command()
async def my_help(ctx):
    await ctx.send("kullanabileceğin kodlar:\n" + "\n".join(help_list))

bot.run(TOKEN)        
