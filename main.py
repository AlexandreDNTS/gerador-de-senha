import PySimpleGUI as sg
from random import randint


def tela_inicial():
    layout = [
        [sg.Text('\n\tGERADOR DE SENHA\t')],
        [sg.Text('tamanho da senha')],
        [sg.Input(key='tam')],
        [sg.Text('Min: 5 Max: 25')],
        [sg.Text('', key='msgtam')],
        [sg.Button('gerar senha')],
        [sg.Text('', key='senha')]
    ]
    return sg.Window('gerador de senha', layout=layout, finalize=True)


telaInicial = tela_inicial()

while True:
    listasenha = []
    window, eventos, valores = sg.read_all_windows()
    if eventos == sg.WIN_CLOSED:
        break

    if window == telaInicial and eventos == 'gerar senha':
        window['senha'].update('')
        if valores['tam'] != '':
            valor = int(valores['tam'])
            if valor < 5 or valor > 25:
                window['senha'].update(
                    'a senha deve ter um tamanho minimo de  5 caractere e um tamanho maximo de 25 caracteres')
            else:
                i = 0
                while i < valor:
                    senha = randint(0, valor)
                    listasenha.append(senha)
                    i += 1
                window['msgtam'].update(listasenha)
        else:
            window['msgtam'].update('digite um tamnho para senha')
