import asyncio
from kucoin.asyncio import KucoinSocketManager
loop = asyncio.get_event_loop()

async def handle_msg(msg):
    # Process incoming messages
    if msg['topic'].startswith('/market/ticker'):
        print(msg['data'])  # live ticker data

async def run_ws():
    ksm = await KucoinSocketManager.create(loop, client, handle_msg)
    await ksm.subscribe('/market/ticker:ETH-USDT')
    while True:
        await asyncio.sleep(10)

loop.run_until_complete(run_ws())
