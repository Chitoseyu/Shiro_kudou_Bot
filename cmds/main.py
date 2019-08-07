import discord
import datetime
import pytz
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):
    
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')
    
    @commands.command()
    async def hi(self,ctx):
        await ctx.send('What?')

    @commands.command()
    async def em(self,ctx):
        
        embed=discord.Embed(title="About me", url="https://www.plurk.com/black7591" , description="about the bot", color=0x1137ee,timestamp=datetime.datetime.now(pytz.timezone('Asia/Shanghai')))
        embed.set_author(name="ShiroNeko", url="https://i.imgur.com/f7daV5o.png", icon_url="https://i.imgur.com/f7daV5o.png")
        embed.set_thumbnail(url="https://i.imgur.com/vXV374R.jpg")
        embed.add_field(name=1, value=11, inline=True)
        embed.add_field(name=2, value=22, inline=True)
        embed.add_field(name=3, value=33, inline=True)
        embed.add_field(name=4, value=44, inline=True)
        embed.set_footer(text="------------------END------------------")
        await ctx.send(embed=embed) 


def setup(bot):
    bot.add_cog(Main(bot))