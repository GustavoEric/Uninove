import PySimpleGUI as sg

sg.theme('DarkAmber')
layout = [
    [sg.Text('Valor:'),sg.InputText()],
    [sg.Text('Desconto:'),sg.InputText()],
    [sg.Button('OK')]
]

window = sg.Window('Aula 06 ',layout)

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'OK':
        valor = float(values[0])
        desconto = float(values[1])
        valor_descontado = valor*((100-desconto)/100)
        valor_aumentado = valor*((100+desconto)/100)
        sg.popup('Valor: ',valor)
        sg.popup('Desconto: ',desconto)
        sg.popup('Valor com Desconto: ',valor_descontado)
        sg.popup('Valor com Aumento: ',valor_aumentado)
window.close()