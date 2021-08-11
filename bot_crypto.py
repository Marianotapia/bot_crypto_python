import discord
from discord.ext import commands, tasks
from urllib3.packages.six import _import_module
from price_pvu import price
from por_crypto import multiplo
import datetime
################## PING ##################
bot = commands.Bot(command_prefix="$",case_insensitive=True)
################## Bot Ready ##################
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.do_not_disturb,  activity=discord.Game("CON TU SEÑORA"))
    print("Bot is ready.")
################## PVU ##################
@bot.command()
async def pvu (ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description=price("PVU"),timestamp=datetime.datetime.utcnow(),color=discord.Color.green())
    embed.set_thumbnail(url="https://plantvsundead.com/assets/img/Logo%20game.png")
    await ctx.send(embed=embed)
################## BTC ##################
@bot.command()
async def btc(ctx):
    embed = discord.Embed(title="BTC", description=price("BTC"),timestamp=datetime.datetime.utcnow(),color=discord.Color.orange())
    embed.set_thumbnail(url="https://logos-marcas.com/wp-content/uploads/2020/08/Bitcoin-Logo.png")
    await ctx.send(embed=embed)
################## MIST ##################
@bot.command()
async def mist(ctx):
    embed = discord.Embed(title="MIST", description=price("MIST"),timestamp=datetime.datetime.utcnow(),color=discord.Color.dark_gold())
    embed.set_thumbnail(url="https://s2.coinmarketcap.com/static/img/coins/200x200/9218.png")
    await ctx.send(embed=embed)
################## ETH ##################
@bot.command()
async def eth(ctx):
    embed = discord.Embed(title="ETH", description=price("ETH"),timestamp=datetime.datetime.utcnow(),color=discord.Color.light_grey())
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/b/b7/ETHEREUM-YOUTUBE-PROFILE-PIC.png")
    await ctx.send(embed=embed)
################## REVO ##################
@bot.command()
async def revo(ctx):
    embed = discord.Embed(title="REVO", description=price("REVO"),timestamp=datetime.datetime.utcnow(),color=discord.Color.blurple())
    embed.set_thumbnail(url="https://miro.medium.com/fit/c/1360/1360/1*w61AxyZpSTDBslJl7-G-tQ.png")
    await ctx.send(embed=embed)
################## ZOON ##################
@bot.command()
async def zoon(ctx):
    embed = discord.Embed(title="ZOON", description=price("ZOON"),timestamp=datetime.datetime.utcnow(),color=discord.Color.red())
    embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/17419/large/logo200_%2820%29.png?1627599450")
    await ctx.send(embed=embed)
################## Ping ##################
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

@bot.command()
async def por(ctx, a: float, message=None):
    await ctx.send((a*(multiplo(message.upper()))))

################## Clear ##################
@bot.command()
async def clear (ctx, amount=5):
    await ctx.channel.purge(limit=amount)
################## Token ##################
bot.run("TOKEN")
