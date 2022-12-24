import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib

import expenditureHandeller
import salesHandeller
import loginHaneller


sales = salesHandeller.sales()
expence = expenditureHandeller.expences()
users = loginHaneller.security()

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

layout1 = [
    [sg.Text('Please enter your Name, Age, Phone')],
    [sg.Text('UserName', size =(15, 1)), sg.InputText(key='-EMAIL-')],
    [sg.Text('Password', size =(15, 1)), sg.InputText('', key='-PASSWORD-', password_char='*', size=(15, 1))],
    [sg.Submit(), sg.Cancel()],
    [sg.Text('', size = (15, 1), font = ('Helvetica', 18),
                text_color = 'black', key = 'input')],
]

layout2= [
    [sg.Text("Hello from PySimpleGUI")], 
    [sg.Button("expence")], [sg.Button("sales")], [sg.Button("INPUT EXPENCE DATA")], [sg.Button("INPUT SALES DATA")] ]

layout3 = [
    [sg.Text('Enter Data')],
    [sg.Text('Name of', size =(15, 1)), sg.InputText(key='-name-')],
    [sg.Text('Amount', size =(15, 1)), sg.InputText(key='-amount-')],
    [sg.Submit(), sg.Cancel()],
    [sg.Text('', size = (15, 1), font = ('Helvetica', 18),
                text_color = 'black', key = 'input')],
]

# ----------- Create actual layout using Columns and a row of Buttons
layout = [[sg.Column(layout1, key='-COL1-'), sg.Column(layout2, visible=False, key='-COL2-'), sg.Column(layout3, visible=False, key='-COL3-')]]


# Create the window
window = sg.Window("Accounting App", layout, size=(500, 500))


loggin = False
# Create an event loop
while True:


    event, values = window.read()

    if loggin == False:
        email_input_value = values['-EMAIL-']
        password_input_value = values['-PASSWORD-']  
        # print(email_input_value)
        # print(password_input_value)

        attempt = users.login_login(email_input_value,password_input_value)
        
        if attempt == False: 
            window.FindElement('input').Update("Invalid Input Try Again")
        else:
            window.FindElement('input').Update("Welcome: Setting up your workspace now...")
            loggin = True

            window[f'-COL1-'].update(visible=False)
            window[f'-COL2-'].update(visible=True)

    else:
        if event == "expence":
            graph_expence()
        elif event == "sales":
            graph_sales()
        elif event == "INPUT EXPENCE DATA":
            window[f'-COL2-'].update(visible=False)
            window[f'-COL3-'].update(visible=True)


            # TODO create a secondary loop of events to get entered amount
            amount = values['-amount-']
            print(amount)

    # End program if user closes window or
    # presses the OK button
    if event == "EXIT" or event == sg.WIN_CLOSED:
        # graph()
        break
    


window.close()