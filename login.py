import PySimpleGUI as sg

def cadastrar_usuario(usuario, senha):
    if verificar_usuario(usuario):
        return 'Usuário já cadastrado'
    else:
        with open('./usuarios.txt', 'w') as f:
            f.write(f'{usuario}:{senha}\n')
        return 'Usuário cadastrado com sucesso!'

def verificar_usuario(usuario, senha=None):
    with open('./usuarios.txt', 'r') as f:
        for linha in f:
            u, s = linha.strip().split(':')
            if u == usuario and (senha is None or s == senha):
                return True
    return False

layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('Login'), sg.Button('Cadastrar')],
    [sg.Text('', key='mensagem')],
]

window = sg.Window('Login', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Cadastrar':
        usuario = values['usuario']
        senha = values['senha']
        mensagem = cadastrar_usuario(usuario, senha)
        window['mensagem'].update(mensagem)
        window['usuario'].update('')
        window['senha'].update('')
    elif event == 'Login':
        usuario = values['usuario']
        senha = values['senha']
        if verificar_usuario(usuario, senha):
            window['mensagem'].update('Login bem-sucedido!')
            window['usuario'].update('')
            window['senha'].update('')
        else:
            window['mensagem'].update('Usuário ou senha incorretos.')