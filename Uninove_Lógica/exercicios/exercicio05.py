import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Usuario'), sg.InputText()],
            [sg.Text('Senha'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
usuario = 'Gustavo'
senha = '1234G'
tentativas = 0
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == 'Ok':
        if  (values[0] == usuario and values [1] == senha):
            sg.popup('Acesso Liberado')
        else:
            tentativas+=1
            sg.popup(f'Acesso Recusado \nQuantidade de tentativas {tentativas}')
        if tentativas == 3:
            window.close()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

window.close()