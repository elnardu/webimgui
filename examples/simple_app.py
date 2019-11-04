from webimgui import run_simple, UiBuilder, Session
from aiohttp import web

import numpy as np
import matplotlib.pyplot as plt


# Run `adev runserver simple_app.py` in the terminal to enable hot reload.
# It takes around 5 seconds for your changes to apply

# Global variabales - available to everyone


def main_dashboard(session: Session):
    # Local variables - available only to the current session

    print("New session created:", session.session_id)
    print(session.client_data)

    def render(ui: UiBuilder):
        # Render variables - available only during layout rendering

        with ui.row():
            with ui.column(size=4):
                ui.h3("Controls:")

                ui.paragraph("Function:")
                function = ui.select("Function", ["sin", "cos"])

                with ui.row():
                    with ui.column():
                        x1, x2 = ui.range_slider("x")
                        ui.paragraph(f"{x1} <= x <= {x2}")

                    with ui.column():
                        offset = ui.slider("offset")
                        ui.paragraph(f"offset: {offset}")

                show_legend = ui.checkbox("Show legend")

                is_red = ui.button("Red", type="danger")

            with ui.column(size=8):
                ui.h3("Plot:")

                plt.figure()

                x = np.arange(x1, x2, 0.0005)
                x += offset

                if function == "sin":
                    y = np.sin(x)
                elif function == "cos":
                    y = np.cos(x)

                if is_red:
                    plt.plot(x, y, "r", label=function)
                else:
                    plt.plot(x, y, label=function)

                if show_legend:
                    plt.legend()

                with ui.center():
                    ui.mpl_plot(plt)

    return render


app = run_simple(main_dashboard)

if __name__ == "__main__":
    web.run_app(app, port=9999)
