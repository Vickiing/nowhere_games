import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Insira a quantidade de roletas'), sg.Input(size=(3),key='roleta')],
            #[sg.Text('Qual é o seu humor?',auto_size_text='Qual é o seu humor?')],
            #[sg.Checkbox('Feliz',auto_size_text='feliz',key='feliz')],
            # [sg.Checkbox('Triste',auto_size_text='feliz',key='triste')],
            # [sg.Text('Digite seu nome'), sg.InputText(key='nome')],
            # [sg.Text("Você é:")],
            # [sg.Checkbox("Crente",auto_size_text="Crente",key='crente'),sg.Checkbox("Desviado",auto_size_text="Desviado",key='desviado')],
            [sg.Button('Ok'), sg.Button('Cancel')],
            [sg.Output(size=(20,5), key='log')]
            ]

window = sg.Window('Loteria do Victor', layout,auto_size_text='Loteria do Victor')

def iniciar(values):
    roleta = int(values['roleta'])
    return roleta

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Ok':
       iniciar(values)
window.close()


