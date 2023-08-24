# aiohttpdemo_polls/main.py
from aiohttp import web
from settings import config
from routes import setup_routes
from db import pg_context
import sys
import asyncio

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = web.Application()
setup_routes(app)
app.cleanup_ctx.append(pg_context)
app['config'] = config
web.run_app(app)