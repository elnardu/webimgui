from .page import Page
from .serve import Serve
from .ui import UiBuilder

def run_simple(function):
    webimgui = Serve({"/": Page(function)})
    return webimgui.app
