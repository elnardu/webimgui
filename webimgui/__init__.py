from .page import Page
from .serve import Serve
from .session import Session
from .ui import UiBuilder


def run_simple(function):
    webimgui = Serve({"/": Page(function)})
    return webimgui.app
