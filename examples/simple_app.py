import sys

sys.path.append("..")

from webimgui import run_simple, UiBuilder
from aiohttp import web

import logging
from webimgui.logging import logger
logger.setLevel(logging.DEBUG)

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

import numpy as np

def main_dashboard(session):
    import matplotlib.pyplot as plt

    print("New session created:", session.session_id)
    print(session.client_data)

    def render(ui: UiBuilder):
        with ui.row():
            with ui.column(size=4):
                ui.h2("Controls:")
                if ui.button("Hello"):
                    ui.paragraph("Bla Bla Bla True")
                else:
                    ui.paragraph("Bla Bla Bla False")

                with ui.same_line():
                    ui.button("Hello", type_="primary")
                    ui.button("Hello", type_="secondary")
                    ui.button("Hello", type_="success")
                    ui.button("Hello", type_="danger")
                    select_choice = ui.select("Simple select", ['Hello', 'World'])

                ui.paragraph(select_choice)

                x1, x2 = ui.range_slider("x", min=0, max=30, step=0.5)
                ui.paragraph(f"{x1} {x2}")

                number = ui.range_slider("Cool Slider 2", step=0.5)
                ui.paragraph(number)

            with ui.column(size=8):
                ui.h2("Plot:")
                plt.figure()
                x = np.arange(x1, x2, 0.0005)
                y = np.sin(x)
                plt.plot(x, y)
                ui.mpl_plot(plt)
                
    return render


app = run_simple(main_dashboard)

if __name__ == "__main__":
    web.run_app(app)
