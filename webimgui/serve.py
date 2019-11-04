from typing import Dict
import os

import socketio
from aiohttp import web

from .exceptions import WebimguiException
from .logging import logger
from .page import Page
from .session import Session

STATIC_FILES_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "dist")


class PageNamespace(socketio.AsyncNamespace):
    def __init__(self, namespace: str, page: Page):
        super().__init__(namespace)
        self.page = page
        self.active_page_sessions = {}

    def get_session(self, sid) -> Session:
        if sid not in self.active_page_sessions:
            raise WebimguiException("Session not found")

        return self.active_page_sessions[sid]

    async def render_layout(self, sid):
        session = self.get_session(sid)
        await self.emit("layout", session._render_layout(), room=sid)

    def on_connect(self, sid, environ):
        logger.debug(f"Sid {sid} connected")

    def on_disconnect(self, sid):
        logger.debug(f"Sid {sid} disconnected")
        if sid in self.active_page_sessions:
            del self.active_page_sessions[sid]

    async def on_initialize(self, sid, data):
        session = self.page.new_session(str(sid))
        session._initialize(data)
        self.active_page_sessions[sid] = session
        await self.emit("configuration", session._get_client_configuration())
        await self.render_layout(sid)

    async def on_action(self, sid, data):
        logger.debug(f"New action: {data}")
        session = self.get_session(sid)
        session._handle_action(data)
        await self.render_layout(sid)


class Serve:
    routes: Dict[str, Page]

    def __init__(self, params):
        if isinstance(params, Page):
            self.routes = {"/": params}
        elif isinstance(params, dict):
            self.routes = params
        else:
            raise TypeError("Invalid type")

        self.sio = socketio.AsyncServer(async_mode="aiohttp", cors_allowed_origins="*")
        self.app = web.Application()

        async def index(request):
            return web.FileResponse(os.path.join(STATIC_FILES_DIR, "index.html"))

        self.app.router.add_route("GET", "/", index)
        self.sio.attach(self.app)
        self.app.router.add_static("/", path=STATIC_FILES_DIR, name="static")

        for namespace in self.routes:
            self.sio.register_namespace(
                PageNamespace(namespace, self.routes[namespace])
            )
