import discord
import praw
import pdb
import re
import os
from discord.ext import commands
reddit=praw.Reddit('bot1')

subreddit = reddit.subreddit("FortNiteBr")
bot = commands.Bot(command_prefix='!', description='A bot that does random stuff')


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

    @commands.command()
    async def mastaIRL(self, ctx):
        """A picture demonstrating masta irl"""
        channel = ctx.message.channel
        with open('data/mycog/sakamotoseat.gif', 'rb') as f:
            await self.bot.send_file(ctx, f)
       
    @commands.command()
    async def greet(self):
        """Greets everyone!"""
        await self.bot.say(":smiley: :wave: Hi senpai!")

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

def setup(bot):
    bot.add_cog(Mycog(bot))
