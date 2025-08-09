
import discord
import os
import random
from discord.ext import commands



async def mems(ctx, folder_path= "images"):
  # resimlerin olduğu klasör
    resim_listesi = []
    for dosya in os.listdir(folder_path):
        if dosya.lower().endswith((".png",".jpg", ".jpeg", ".gif")):
            """dosya adlı değişkeni resim dosyaları ile eşliyor."""
            resim_listesi.append(os.path.join(folder_path, dosya))

    # Sıra sıra gönder
    for resim_yolu in resim_listesi:
        with open(resim_yolu, "rb") as f:
            picture = discord.File(f)
            await ctx.send(file=picture)

async def all_mems(ctx, folder_path= "images"):
    all_mem = os.listdir(folder_path)
    rastgele_mens = random.choice(all_mem)
    full_path = os.path.join(folder_path,rastgele_mens) # Dosya yolunu birleştir
    try:
        with open(full_path, "rb") as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    except:
        print("kodun bir boka yaramıyor.")        