import asyncio
import websockets
import json
import random
import time

async def price_feed(websocket, path):
    while True:
        now = int(time.time()) * 1000
        price = round(random.uniform(101, 104), 2)
        bar = {
            "time": now,
            "open": price - 0.5,
            "high": price + 0.8,
            "low": price - 1.2,
            "close": price,
            "volume": random.randint(1000, 3000)
        }
        await websocket.send(json.dumps(bar))
        await asyncio.sleep(1)

start_server = websockets.serve(price_feed, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
print("✅ WebSocket server running at ws://localhost:8765")
asyncio.get_event_loop().run_forever()
