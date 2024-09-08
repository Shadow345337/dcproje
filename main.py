import discord
from discord.ext import commands
from shaco import model
from tokkeenn import tokenn
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def kontrol(ctx):
    if ctx.message.attachments:
        for resim in ctx.message.attachments:
            resim_ismi = resim.filename
            resim_url = resim.url
            await resim.save(f"./{resim.filename}")
            await ctx.send(f"Resim başarısızlıkla kaydedildi{resim.filename}")
            await ctx.send(model(model_ismi="./keras_model.h5",labels="labels.txt",resim=f"./{resim.filename}"))
    else :
        await ctx.send("fotoğraf yok ekle")

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run(tokenn)