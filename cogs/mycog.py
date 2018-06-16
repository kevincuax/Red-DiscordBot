import discord
from bs4 import BeautifulSoup
import requests
import webbrowser
import praw
import pdb
import re
import os
import datetime
import asyncio
import aiohttp
from discord.ext import commands
reddit=praw.Reddit('bot1')

subreddit = reddit.subreddit("FortNiteBr")
bot = commands.Bot(command_prefix='!', description='A bot that does random stuff')

client = discord.Client()

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def topSubmissions(self, *, subName):
        """Get the top 5 hot posts for any subreddit"""

        #Your code will go here
        subreddit = reddit.subreddit(subName);
        for submission in subreddit.hot(limit=5):
            await self.bot.say(submission.url)
    @commands.command()      
    async def wordSearch(self, subName, *, word):
        """Count the # of times a word is said in a subreddit"""
        #test
        wordCount = 0
               # cehck top 10
        subreddit = reddit.subreddit(subName);    
        for submission in subreddit.hot(limit=10):
        
                # do a case insensitive search
                if re.search(word, submission.title, re.IGNORECASE):
                    # increase counter
                    wordCount += 1
                    await self.bot.say(submission.url)
            
                              #output word count
        await self.bot.say(word + " is included in " + repr(wordCount) + " titles")

    @commands.command(pass_context = True)
    async def mastaIRL(self, ctx):
        """A picture demonstrating masta irl"""
        channel = ctx.message.channel
        with open('data/mycog/sakamotoseat.gif', 'rb') as f:
            await self.bot.send_file(ctx, f)
       
    @commands.command()
    async def greet(self, member: discord.Member):
        """Greets everyone!"""
        await self.bot.say(":smiley: :wave: Hi {0.name} senpai!".format(member))

    @commands.command()
    async def about(self):
    
        embed = discord.Embed(title="Red Discord bot", description="An instance of red discord bot.")
    
        # author info
        embed.add_field(name="Author", value="Remonwater")

        await self.bot.say(embed=embed)

    @commands.command(pass_context = True)
    async def invite(self, ctx, userToInvite):
        inviteLink = await self.bot.create_invite(destination = ctx.message.channel, xkcd = True, max_uses = 1)
        target_member = ctx.message.server.get_member_named(userToInvite)
        await self.bot.send_message(target_member, inviteLink)  
    @commands.command()
    async def role(self, member: discord.Member):
        """Lists the roles of a certain user"""
        await self.bot.say('{0.name} has roles {0.role}'.format(member))
        
     
    @commands.command()
    async def joined(self, member: discord.Member):
        """Says when a member joined."""
        await self.bot.say('{0.name} joined in {0.joined_at}'.format(member))

    @commands.command(name='add', aliases=['plus'])
    async def do_addition(self, first: int, second: int):
        """Addition command"""
        
        total = first + second
    
        await self.bot.say(first + second)
    @commands.command(pass_context = True)
    async def roles(self, ctx):
        """Displays all roles with IDS"""
        roles = ctx.message.server.roles
        result = "The roles are "
        for role in roles:
            result += role.name + ": " + role.id + ", "
        await self.bot.say(result)
   
    @commands.command(pass_contex = True)
    async def google(self, text):
        """Googles something"""
        text = urllib.parse.quote_plus(text)
        
        url = 'https://google.com/search?q=' + text
        
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        for g in soup.find_all(class_='g'):
            await self.bot.say(g.text)
    @commands.command(pass_context = True)
    async def weather(self):
        """Get the weather"""
        
        page = requests.get("https://forecast.weather.gov/MapClick.php?lat=38.2492&lon=-122.0439#.WyR1zO4vyUk")
        soup = BeautifulSoup(page.content, 'html.parser')
        seven_day = soup.find(id="seven-day-forecast")
        forecast_items = seven_day.find_all(class_="tombstone-container")
        tonight = forecast_items[0]
  
        period = tonight.find(class_="period-name").get_text()
        short_desc = tonight.find(class_="short-desc").get_text()
        temp = tonight.find(class_="temp").get_text()
        await self.bot.say(period)
        await self.bot.say(short_desc)
        await self.bot.say(temp)
 
    
def setup(bot):
    bot.add_cog(Mycog(bot))   

