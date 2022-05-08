from PySimpleGUI import PySimpleGUI as psg

#Layout
psg.theme('DarkBlue1')
layout = [
    [psg.Text('Usuário'), psg.Input(key='usuario', size = (24,1))],
    [psg.Text('Senha'), psg.Input(key='senha', password_char='*', size = (24,1))],
    [psg.Checkbox('Salvar o login?')],
    [psg.Button('Entrar')]
]
#Janela
janela = psg.Window('Tela de login', layout)

#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == psg.WINDOW_CLOSED:
        print('Até a próxima.')
        break
    if eventos == 'Entrar:':
        if valores['usuario'] == 'fernando' and valores['senha'] \
        =='fernando':
            print('Seja bem vindo!')
        else:
            print('Credenciais inválidas, tente novamente.')
