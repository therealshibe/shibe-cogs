from num2words import num2words
from discord.ext import commands
from word2number import w2n

class spellnum:
    """Shows the word of a number"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def spellnum(self, context, num):
        """spellnum"""
        i = int(num)
        wordnum = num2words(i)
        await self.bot.say(wordnum)

    @commands.command(pass_context=True)
    async def wordnum(self, context, word):
        """wordnum"""
        wordnum = w2n.word_to_num(word)
        await self.bot.say(wordnum)


def setup(bot):
    bot.add_cog(spellnum(bot))
