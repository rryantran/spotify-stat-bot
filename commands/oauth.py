from discord.ext import commands


class OAuth(commands.Cog):
    """Cog for Spotify OAuth commands"""

    def __init__(self, bot):
        self.bot = bot
        self.flask_url = "http://127.0.0.1:5000/login"

    @commands.command(name="linkspotify")
    async def link_spotify(self, ctx):
        """Links your Spotify account to the bot"""

        await ctx.send(f"Click this link to link your Spotify account: {self.flask_url}")


async def setup(bot):
    await bot.add_cog(OAuth(bot))
