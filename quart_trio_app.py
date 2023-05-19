import asyncio
import trio # 855f5fd  https://github.com/python-trio/trio/archive/refs/heads/master.zip
from quart import Quart # c87bb79  https://github.com/pallets/quart/archive/refs/heads/main.zip
from quart_trio import QuartTrio # 639d59c  https://github.com/pgjones/quart-trio/archive/refs/heads/main.zip

app = QuartTrio(__name__)
#app = Quart(__name__)

@app.route('/')
async def endpoint():
    return {"hello": "world"}

@app.route('/trio')
async def ttest():
    await trio.sleep(5)
    return 'OK Trio'  

@app.route('/asyncio')
async def atest():
    await asyncio.sleep(5)
    return 'OK Asyncio'  

app.run()
