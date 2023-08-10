import PySimpleGUI as sg

sg.theme('DarkAmber')

valor=''
def create_layout(valor):
    layout = [
        [sg.InputText(valor,size=(100,70))],
        [sg.Button('()'),sg.Button('%'),sg.Button('/')],
        [sg.Button('+'),sg.Button('x'),sg.Button('-')],
        [sg.Button('Divisão Inteira'),sg.Button('='),sg.Button('Exponenciação')]
    ]
    return sg.Window('Window ',layout)
window = create_layout(valor) 
def update_layout(valorOP,operador):
    valor = valorOP
    valor+=operador
    return valor

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event =='+':
        window.close
        window = create_layout(update_layout(values[0], '+'))
    elif event =='x':
        window.close
        window = create_layout(update_layout(values[0], 'x'))
    elif event =='-':
        window.close
        window = create_layout(update_layout(values[0], '-'))
    elif event =='/':
        window.close
        window = create_layout(update_layout(values[0], '/'))
    elif event =='Divisão Inteira':
        resultado = int(values[0])//int(values[1])
    elif event =='=':
        sg.popup(values[0])
    elif event =='Exponenciação':
        resultado = int(values[0])**int(values[1])
    text = values[0]
window.close