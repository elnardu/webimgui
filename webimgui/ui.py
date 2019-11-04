from io import StringIO
from typing import Dict, List

from .components import (
    H1,
    H2,
    H3,
    SVG,
    BaseContextComponent,
    Button,
    Checkbox,
    Column,
    Container,
    FlexboxLine,
    HorizontalCenter,
    Paragraph,
    RangeSlider,
    Row,
    Select,
    Slider,
)


class UiBuilder:
    def __init__(self, interactive_elements_state: Dict):
        self._interactive_elements_state = interactive_elements_state
        self._element_stack: List[BaseContextComponent] = [Container(self)]

    def _add_element(self, element):
        self._element_stack[-1].add_child(element)

    def _push_element_to_stack(self, element: BaseContextComponent):
        self._element_stack.append(element)

    def _pop_element_from_stack(self):
        assert (
            len(self._element_stack) > 1
        ), "At least one element should remain on the element stack"

        self._add_element(self._element_stack.pop())

    def _build(self):
        assert len(self._element_stack) == 1
        root = self._element_stack[0]
        return {"layout": root.build(), "state": self._interactive_elements_state}

    # Interactive elements
    def button(self, label: str, type: str = "secondary") -> bool:
        self._add_element(Button(self, label, type))

        if label not in self._interactive_elements_state:
            self._interactive_elements_state[label] = False

        return self._interactive_elements_state[label]

    def select(self, label: str, choices: List[str]) -> str:
        assert len(choices) != 0, "choices cannot be empty"
        self._add_element(Select(self, label, choices))

        if label not in self._interactive_elements_state:
            self._interactive_elements_state[label] = choices[0]

        return self._interactive_elements_state[label]

    def checkbox(self, label: str) -> bool:
        self._add_element(Checkbox(self, label))

        if label not in self._interactive_elements_state:
            self._interactive_elements_state[label] = False

        return self._interactive_elements_state[label]

    def slider(
        self, label: str, min: float = 0.0, max: float = 100.0, step: float = 1.0
    ) -> float:
        assert min < max, "min cannot be larger than max"
        self._add_element(Slider(self, label, min, max, step))

        if label not in self._interactive_elements_state:
            self._interactive_elements_state[label] = min

        return self._interactive_elements_state[label]

    def range_slider(
        self, label: str, min: float = 0.0, max: float = 100.0, step: float = 1.0
    ) -> float:
        assert min < max, "min cannot be larger than max"
        self._add_element(Slider(self, label, min, max, step))

        if label not in self._interactive_elements_state:
            self._interactive_elements_state[label] = [min, max]

        return tuple(self._interactive_elements_state[label])

    # Non iteractive elements
    def h1(self, text) -> None:
        self._add_element(H1(self, text))

    def h2(self, text) -> None:
        self._add_element(H2(self, text))

    def h3(self, text) -> None:
        self._add_element(H3(self, text))

    def paragraph(self, text: str) -> None:
        self._add_element(Paragraph(self, text))

    # Flow control elements
    def same_line(self) -> FlexboxLine:
        return FlexboxLine(self)

    def center(self) -> HorizontalCenter:
        return HorizontalCenter(self)

    def row(self) -> Row:
        return Row(self)

    def column(self, size=None) -> Column:
        if size:
            assert 0 < size and size <= 12, "size must be between 1 and 12"
        return Column(self, size)

    # Plots
    def mpl_plot(self, plot) -> None:
        path = StringIO()
        plot.savefig(path, format="svg")
        path.seek(0)
        self._add_element(SVG(self, path.read()))
