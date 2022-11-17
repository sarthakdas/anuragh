import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib

import expenditureHandeller
import salesHandeller


sales = salesHandeller.sales()
expence = expenditureHandeller.expences()

def graph_expence():
    fig = matplotlib.figure.Figure(figsize=(5, 5), dpi=100)
    x,y = expence.datareturn()
    # a = plot.bar
    fig.add_subplot(111,).bar(x,y)

    matplotlib.use("TkAgg")

    # Define the window layout
    layout = [
        [sg.Text("Total Expenditure")],
        [sg.Canvas(key="-CANVAS-")],
        [sg.Button("Ok")],
    ]

    # Create the form and show it without the plot
    window = sg.Window(
        "Matplotlib Single Graph",
        layout,
        location=(0, 0),
        finalize=True,
        element_justification="center",
        font="Helvetica 18",
    )
    # Add the plot to the window
    draw_figure(window["-CANVAS-"].TKCanvas, fig)

    event, values = window.read()

def graph_sales():
    fig = matplotlib.figure.Figure(figsize=(5, 5), dpi=100)
    x,y = sales.datareturn()
    # a = plot.bar
    fig.add_subplot(111,).plot(x,y)

    matplotlib.use("TkAgg")

    # Define the window layout
    layout = [
        [sg.Text("Total Sales")],
        [sg.Canvas(key="-CANVAS-")],
        [sg.Button("Ok")],
    ]

    # Create the form and show it without the plot
    window = sg.Window(
        "Matplotlib Single Graph",
        layout,
        location=(0, 0),
        finalize=True,
        element_justification="center",
        font="Helvetica 18",
    )
    # Add the plot to the window
    draw_figure(window["-CANVAS-"].TKCanvas, fig)

    event, values = window.read()


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("expence")], [sg.Button("sales")]]

# Create the window
window = sg.Window("Demo", layout)


# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "EXIT" or event == sg.WIN_CLOSED:
        # graph()
        break
    
    if event == "expence":
        graph_expence()
    elif event == "sales":
        graph_sales()

window.close()