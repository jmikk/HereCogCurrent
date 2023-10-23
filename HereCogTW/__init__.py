from .HereCogTW import HereCogTW


async def setup(bot):
    await bot.add_cog(HereCogTW(bot))
