#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Allan Ni'

''' 
async web application.
'''

import logging; logging.basicConfig(levle=logging.INFO)
import asyncio, os, json, time`
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Allan</h1>', content_type='text/html')