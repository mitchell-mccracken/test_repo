import PySimpleGUI as sg
import math

sg.theme('DarkAmber')

layout = [  [sg.Text('enter A'), sg.InputText('0', key='A_Text')],
            [sg.Text('enter B'), sg.InputText('0', key = 'B_Text')],
            [sg.Button('C', key='C_Button'), sg.InputText('0', key='C_Text')],
            #[sg.Text('Enter something on Row 2'), sg.InputText()],
            #[sg.Combo(('choice 1','choice 2'),size=(20,1))],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break
    if event == 'C_Button':
        print('you clicked the button')
        a=float(values['A_Text'])
        b=float(values['B_Text'])
        c=math.sqrt(a**2 + b**2)
        window['C_Text'].update(c)
        
window.close()
