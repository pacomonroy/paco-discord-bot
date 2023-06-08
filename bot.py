import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel is not None and after.channel.name == "🎮- main":
        channel = discord.utils.get(member.guild.text_channels, name='🌐-general')
        if channel:
            await channel.send(f'{member.name} has joined {after.channel.name} voice channel.')
        

bot.run('YOUR BOT TOKEN HERE')
