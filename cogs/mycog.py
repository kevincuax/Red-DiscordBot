import discord
#!/usr/bin/python
import praw

reddit=praw.Reddit('bot1')

subreddit = reddit.subreddit("FortNiteBr")

from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def topReddit(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say(submission.title)


def setup(bot):
    bot.add_cog(Mycog(bot))
