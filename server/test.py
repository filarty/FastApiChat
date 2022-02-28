import asyncio
import websockets


async def hello():
    async with websockets.connect("ws://127.0.0.1:2000/ws") as websocket:
        await websocket.send("Hello world!")
        await websocket.recv()


asyncio.run(hello())
