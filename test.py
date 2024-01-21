from appy_graphql.albert_heijn_api import AlbertHeijn
import asyncio
import aiohttp


async def auth():
    async with aiohttp.ClientSession() as session:
        ah = AlbertHeijn(session)
        authResult = await ah.authorize('...')
        print(authResult)
        await session.close()


async def refresh():
    async with aiohttp.ClientSession() as session:
        ah = AlbertHeijn(session, '...')
        refreshResult = await ah.refresh('')
        print(refreshResult)
        await session.close()


async def basket():
    async with aiohttp.ClientSession() as session:
        ah = AlbertHeijn(session, '...')
        basketResult = await ah.getBasket()
        print(basketResult)
        await session.close()

async def productSearch():
    async with aiohttp.ClientSession() as session:
        ah = AlbertHeijn(session, '...')
        await ah.productSearch('')
        await session.close()


# asyncio.run(auth())
# asyncio.run(basket())
# asyncio.run(productSearch())
