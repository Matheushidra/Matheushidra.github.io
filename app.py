from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# ROTA PRINCIPAL - AGORA PROTEGIDA
@app.route("/")
def hello_world():
    # Verifica se o usuário está logado antes de mostrar a página
    if not session.get('logged_in'):
        # Se não estiver logado, redireciona para a página de login
        return redirect(url_for('login'))
    # Se estiver logado, mostra a página principal
    return render_template("index.html")

# ROTA PROJETO 1 - TAMBÉM PROTEGIDA
@app.route("/projeto1")
def projeto1():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template("projeto1.html")

# ROTA DE LOGIN
@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form.get('username') == 'admin' and request.form.get('password') == '1234':
            session['logged_in'] = True
            # MUDANÇA: Agora redireciona para a página principal
            return redirect(url_for('hello_world'))
        else:
            error = "Credenciais inválidas. Tente novamente."
            
    return render_template("login.html", error=error)

# ROTA DE LOGOUT
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    # Após sair, redireciona para a página de login
    return redirect(url_for('login'))