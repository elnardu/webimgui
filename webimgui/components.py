from typing import Dict, List, Union

# Base definitions
class BaseComponent:
    ui_builder: "UiBuilder"

    def __init__(self, ui_builder: "UiBuilder", meta: Dict = None):
        self.ui_builder: "UiBuilder" = ui_builder
        self.meta = meta if meta else {}

    def get_type(self):
        raise NotImplementedError

    def build(self):
        return {"type": self.get_type(), "meta": self.meta}


class BaseContextComponent(BaseComponent):
    def __init__(self, ui_builder: "UiBuilder", meta: Dict = None):
        super().__init__(ui_builder, meta)
        self.children = []

    def add_child(self, component: BaseComponent):
        self.children.append(component)

    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, type, value, tb):
        raise NotImplementedError

    def build(self):
        return {
            "type": self.get_type(),
            "meta": self.meta,
            "children": [element.build() for element in self.children],
        }


# Interactive elements
class Button(BaseComponent):
    def __init__(self, ui_builder: "UiBuilder", label: str, type: str):
        super().__init__(ui_builder, {"label": label, "type": type})

    def get_type(self):
        return "button"


class Select(BaseComponent):
    def __init__(self, ui_builder: "UiBuilder", label: str, choices: List[str]):
        super().__init__(ui_builder, {"label": label, "choices": choices})

    def get_type(self):
        return "select"


class Checkbox(BaseComponent):
    def __init__(self, ui_builder: "UiBuilder", label: str):
        super().__init__(ui_builder, {"label": label})

    def get_type(self):
        return "checkbox"


class Slider(BaseComponent):
    def __init__(
        self,
        ui_builder: "UiBuilder",
        label: str,
        min: float = 0.0,
        max: float = 100.0,
        step: float = 1.0,
    ):
        super().__init__(
            ui_builder, {"label": label, "min": min, "max": max, "step": step}
        )

    def get_type(self):
        return "slider"


class RangeSlider(BaseComponent):
    def __init__(
        self,
        ui_builder: "UiBuilder",
        label: str,
        min: float = 0.0,
        max: float = 100.0,
        step: float = 1.0,
    ):
        super().__init__(
            ui_builder, {"label": label, "min": min, "max": max, "step": step}
        )

    def get_type(self):
        return "range-slider"


# Non iteractive elements
class Paragraph(BaseComponent):
    def __init__(self, ui_builder: "UiBuilder", text: str):
        super().__init__(ui_builder, {"text": text})

    def get_type(self):
        return "p"


class BaseHeading(BaseComponent):
    def __init__(self, ui_builder: "UiBuilder", text: str):
        super().__init__(ui_builder, {"text": text})

    def get_type(self):
        raise NotImplementedError


class H1(BaseHeading):
    def get_type(self):
        return "h1"


class H2(BaseHeading):
    def get_type(self):
        return "h2"


class H3(BaseHeading):
    def get_type(self):
        return "h3"


# Flow control elements
class Container(BaseContextComponent):
    def get_type(self):
        return "container-fluid"

    def __enter__(self):
        self.ui_builder._push_element_to_stack(self)

    def __exit__(self, type, value, tb):
        self.ui_builder._pop_element_from_stack()


class HorizontalCenter(BaseContextComponent):
    def get_type(self):
        return "hcenter"

    def __enter__(self):
        self.ui_builder._push_element_to_stack(self)

    def __exit__(self, type, value, tb):
        self.ui_builder._pop_element_from_stack()


class Row(BaseContextComponent):
    def get_type(self):
        return "row"

    def __enter__(self):
        self.ui_builder._push_element_to_stack(self)

    def __exit__(self, type, value, tb):
        self.ui_builder._pop_element_from_stack()


class Column(BaseContextComponent):
    def __init__(self, ui_builder: "UiBuilder", size: Union[None, int]):
        super().__init__(ui_builder, {"size": size})

    def get_type(self):
        return "column"

    def __enter__(self):
        self.ui_builder._push_element_to_stack(self)

    def __exit__(self, type, value, tb):
        self.ui_builder._pop_element_from_stack()


class FlexboxLine(BaseContextComponent):
    def get_type(self):
        return "flexbox-line"

    def __enter__(self):
        self.ui_builder._push_element_to_stack(self)

    def __exit__(self, type, value, tb):
        self.ui_builder._pop_element_from_stack()


# Plots
class SVG(BaseComponent):
    def __init__(self, ui_builder: "UiBuilder", svg: str):
        super().__init__(ui_builder, {"svg": svg})

    def get_type(self):
        return "svg"
