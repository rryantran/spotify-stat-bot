from discord.ext import commands


class OAuth(commands.Cog):
    """Cog for Spotify OAuth commands"""

    def __init__(self, bot):
        self.bot = bot
        self.flask_url = "http://127.0.0.1:3000/login"

    @commands.command(name="linkspotify")
    async def link_spotify(self, ctx):
        """Links your Spotify account to the bot"""
        user_id = str(ctx.author.id)
        auth_url = f"{self.flask_url}?user_id={user_id}"
        await ctx.send(f"Click this link to link your Spotify account: {auth_url}")


async def setup(bot):
    await bot.add_cog(OAuth(bot))
