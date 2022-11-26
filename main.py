import PySimpleGUI as sg
from random import randint


def tela_inicial():
    layout = [
        [sg.Text('\n\tGERADOR DE SENHA\t')],
        [sg.Text('tamanho da senha')],
        [sg.Input(key='tam')],
        [sg.Text('Min: 5 Max: 25')],
        [sg.Text('', key='msgtam')],
        [sg.Radio('numerico', 'gerasenha', key='numerico'),
         sg.Radio('alfabeto', 'gerasenha', key='alfabeto')],
        [sg.Button('gerar senha')],
        [sg.Text('', key='senha')]
    ]
    return sg.Window('gerador de senha', layout=layout, finalize=True)


telaInicial = tela_inicial()

while True:
    listaalfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                     'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    listasenha = []
    listasenhaalfab = []
    window, eventos, valores = sg.read_all_windows()
    if eventos == sg.WIN_CLOSED:
        break

    if window == telaInicial and eventos == 'gerar senha':
        window['senha'].update('')
        if valores['tam'] != '':
            if valores['numerico'] == True:
                valor = int(valores['tam'])
                if valor < 5 or valor > 25:
                    window['senha'].update(
                        'a senha deve ter um tamanho minimo de  5 caractere e um tamanho maximo de 25 caracteres')
                else:
                    i = 0
                    while i < valor:
                        senha = randint(0, 9)

                        listasenha.append(senha)

                        i += 1
                    window['msgtam'].update(listasenha)
            if valores['alfabeto'] == True:
                valor = int(valores['tam'])
                if valor < 5 or valor > 25:
                    window['senha'].update(
                        'a senha deve ter um tamanho minimo de  5 caractere e um tamanho maximo de 25 caracteres')
                else:
                    i = 0
                    while i < valor:

                        listasenhaalfab.append(listaalfabeto[randint(0, 26)])

                        i += 1
                    window['msgtam'].update(listasenhaalfab)
        else:
            window['msgtam'].update('digite um tamnho para senha')
