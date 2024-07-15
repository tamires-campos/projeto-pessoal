from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def is_valid_username(username):
    import re
    username_regex = re.compile(r'[!@#$_-]')
    return bool(username_regex.search(username))

def is_valid_password(password):
    import re
    password_regex = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$')
    return bool(password_regex.match(password))

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['usuario']
        password = request.form['senha']
        if not is_valid_username(username):
            error_message = 'O nome de usuário deve conter pelo menos um dos seguintes caracteres: !@#$_-'
            return render_template('login.html', error_message=error_message)
        if not is_valid_password(password):
            error_message = 'A senha deve conter pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial (!@#$%^&*).'
            return render_template('login.html', error_message=error_message)
        # Se a validação passar, redirecionar para a página específica
        return redirect('https://tamires-campos.github.io/projeto-cordel/')  #AQUI A GENTE ALTERA PARA NOVA PÁGINA
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
