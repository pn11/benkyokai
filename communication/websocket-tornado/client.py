import sys
import websockets
import asyncio

async def test():
    async with websockets.connect('ws://localhost:8888/socket') as ws:
        await ws.send("hello")
        response = await ws.recv()
        print(response)

asyncio.get_event_loop().run_until_complete(test())
