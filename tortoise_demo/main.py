import asyncio

from tortoise import Tortoise

from tortoise_demo.models import Tournament, Event, Team


async def init():
    await Tortoise.init(db_url='sqlite://db.sqlite3',
                        modules={'models': ['tortoise_demo.models']})
    await Tortoise.generate_schemas(safe=True)


async def main():
    await init()
    tournament = Tournament(name='New Tournament')
    await tournament.save()

    await Tortoise.close_connections()


asyncio.run(main())
