import random
import time
from termcolor import colored
import PySimpleGUI as sg
from tela import iniciar

sg.theme('DarkAmber')

layout = [
    [sg.Text('Insira a quantidade de roletas'), sg.Input(size=(3), key='roleta')],
    [sg.Button('Ok'), sg.Button('Cancel')],
    [sg.Multiline(size=(50, 10), key='log', autoscroll=True)]
]

window = sg.Window('Loteria do Victor', layout, auto_size_text='Loteria do Victor')

def iniciar_jogo(roleta):
    Saldo = 1000  # Substitua pelo valor desejado
    roleta_automatica = roleta

    while roleta_automatica > 1:
        if Saldo <= 0:
            break

        lista1_usuario = range(5)
        lista2_pc = range(5)
        num2_aleatorio_pc = []
        num1_aleatorio_usuario = []

        for _ in lista1_usuario:
            num1_aleatorio_usuario.append(random.randint(1, 20))
        window['log'].print(f'Números do Usuário: {num1_aleatorio_usuario}')

        for _ in lista2_pc:
            num2_aleatorio_pc.append(random.randint(1, 20))
        window['log'].print(f'Números do PC: {num2_aleatorio_pc}')

        resultado = set(num2_aleatorio_pc).intersection(num1_aleatorio_usuario)
        window['log'].print(f'Resultado: {resultado}')

        if len(resultado) >= 3:
            Saldo = Saldo + 230
            window['log'].print(colored(f'Você ganhou! Saldo atual: {Saldo}', 'green'))
            time.sleep(2)
        else:
            Saldo = Saldo - 50
            window['log'].print(colored(f'Você perdeu! Saldo atual: {Saldo}', 'red'))
            time.sleep(2)
            roleta_automatica = roleta_automatica - 1

        window.Refresh()

    window['log'].print('Roleta finalizada')

while True:
    event, values = window.read(timeout=100)  # Adiciona timeout para permitir a atualização da janela
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Ok':
        roleta_valor = int(values['roleta'])
        iniciar_jogo(roleta_valor)

window.close()

