import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Digite a quantidade que irá contar'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    pares= []
    impares = []
    maior = []
    if event == 'Ok':
        x=1
        for x in range(int(values[0])+1):
            if  x%2 == 0:
                pares.append(x)
            else:
                impares.append(x)
            if  x >= 18:
                maior.append(x)
        sg.popup(f'Numeros Pares:\n{pares} \nNumeros Impares:\n{impares}\nNumeros Maiores que 18:\n{maior}')
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

window.close()