import discord
from discord.ext import commands
from discord import app_commands

from myserver import server_on

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("คุณต้องอยู่ในช่องเสียงก่อน!")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("บอทไม่ได้อยู่ในช่องเสียง!")

@bot.command()
async def play(ctx, url: str):
    if not ctx.voice_client:
        await ctx.invoke(join)
    
    FFMPEG_OPTIONS = {'options': '-vn'}
    YDL_OPTIONS = {'format': 'bestaudio'}
    
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
        ctx.voice_client.play(source)
    
    await ctx.send(f'กำลังเล่น: {info["title"]}')

server_on()

bot.run("d77553f807da9d3e2ae74553cda366ca77ba269f832049d513e03d06dd2c9fe3")