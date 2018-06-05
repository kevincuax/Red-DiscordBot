import discord
import praw
import pdb
import re
import os

reddit=praw.Reddit('bot1')

subreddit = reddit.subreddit("FortNiteBr")

from discord.ext import commands

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
            
                              #output word count
        await self.bot.say(word + " is included in " + repr(wordCount) + " titles")


def setup(bot):
    bot.add_cog(Mycog(bot))
