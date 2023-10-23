from .HereCog import HereCog


async def setup(bot):
    await bot.add_cog(HereCog(bot))
