from .HereCogz import HereCogz


async def setup(bot):
    await bot.add_cog(HereCogz(bot))
