import PySimpleGUI as sg


def tela_inicial():
    layout = [
        [sg.Text('\n\tGERADOR DE SENHA\t')],
        [sg.Text('tamanho da senha')],
        [sg.Text('', key='msgtam')],
        [sg.Input(key='tam')],
        [sg.Button('gerar senha')],
        [sg.Text('', key='senha')]
    ]
    return sg.Window('gerador de senha', layout=layout, finalize=True)


telaInicial = tela_inicial()

while True:
    window, eventos, valores = sg.read_all_windows()
    if eventos == sg.WIN_CLOSED:
        break
