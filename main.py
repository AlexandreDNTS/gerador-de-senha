import PySimpleGUI as sg
from random import randint


def tela_inicial():
    layout = [
        [sg.Text('\n\tGERADOR DE SENHA\t')],
        [sg.Text('tamanho da senha')],
        [sg.Input(key='tam')],
        [sg.Text('', key='msgtam')],
        [sg.Button('gerar senha')],
        [sg.Text('', key='senha')]
    ]
    return sg.Window('gerador de senha', layout=layout, finalize=True)


telaInicial = tela_inicial()

while True:
    window, eventos, valores = sg.read_all_windows()
    if eventos == sg.WIN_CLOSED:
        break
    if window == telaInicial and eventos == 'gerar senha':
        valor = int(valores['tam'])
        if valor >= 5:
            TAM = valor
            for i in range(0, TAM):
                s = randint(0, TAM)

                window['senha'].update(f'{s}')

        else:
            window['msgtam'].update('tamanho minimo 5')
