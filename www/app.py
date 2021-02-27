#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Allan Ni'

''' 
async web application.
'''

import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    text = b'<h1>Allan</h1>'
    return web.Response(body=text, content_type='text/html')   # content_type='text/html'  不添加会变成下载文件非直接浏览

async def init(loop):
    app = web.Application()
    app.router.add_route('GET', '/', index)
    runner = web.AppRunner(app)
    await runner.setup()
    srv = web.TCPSite(runner, '127.0.0.1', 9000)
    await srv.start()
    logging.info('server start at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()



