import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [
    [sg.Combo(['x = 2Y+Z','x = Y+K+3Z/4'],key='op')],
    #[sg.Text('Valor de Y')],
    #[sg.InputText()],
    #[sg.Text('Valor de Z')],
    #[sg.InputText()],
    [sg.Button('OK')],
]
window = sg.Window('Calcular X',layout)
def op1():
    layout = [
        [sg.Text('Valor de Y')],
        [sg.InputText()],
        [sg.Text('Valor de Z')],
        [sg.InputText()],
        [sg.Button('Calcular')],
    ]
    return sg.Window('Window ',layout)
def op2():
    layout = [
        [sg.Text('Valor de Y')],
        [sg.InputText()],
        [sg.Text('Valor de K')],
        [sg.InputText()],
        [sg.Text('Valor de Z')],
        [sg.InputText()],
        [sg.Button('Calcular')],
    ]
    return sg.Window('Window ',layout)
while True:
    opc=0
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'OK':
        sg.popup("Valor X: ",values['op'])
        if values['op'] == 'x = 2Y+Z':
            opc=1
            window.close
            window = op1()
            op=1
        elif values['op'] == 'x = Y+K+3Z/4':
            opc=2
            window.close
            window = op2()
            op=2
    if event == 'Calcular':
        if op == 1:
            y = int(values[0])
            z = int(values[1])
            x = y*2+z
            sg.popup(x)
        if op == 2:
            y = int(values[0])
            k = int(values[1])
            z = int(values[2])
            x = (y+k+3*z)/4
            sg.popup(x)
       
window.close