from typing import Callable

from .session import Session


class Page:
    def __init__(self, new_page_callable, title=None):
        self.new_page_callable = new_page_callable
        self.title = title if title else new_page_callable.__name__

    def new_session(self, session_id: str) -> Session:
        return Session(self, session_id)
