from .ui import UiBuilder


class Session:
    def __init__(self, page: "Page", session_id: str):
        self.page: "Page" = page
        self.render = None
        self.session_id = session_id
        self.client_data = None
        self.update_interval = "auto"
        self._interactive_elements_state = {}

    def _initialize(self, client_data):
        self.client_data = client_data
        self.render = self.page.new_page_callable(self)

    def _get_client_configuration(self):
        return {"title": self.page.title, "update_interval": self.update_interval}

    def _render_layout(self):
        ui = UiBuilder(self._interactive_elements_state)
        self.render(ui)

        return ui._build()

    def _handle_action(self, action):
        self._interactive_elements_state[action["label"]] = action["data"]

    def set_update_interval(self, update_interval):
        assert (
            isinstance(update_interval, int)
            or isinstance(update_interval, float)
            or update_interval == "auto"
        ), "Invalid type"

        self.update_interval = update_interval
