# Mudança 1: Importamos a nova função 'render_template'
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    # Mudança 2: Trocamos o texto simples pela chamada da nova função
    return render_template("index.html")

# ADICIONE ESTE NOVO BLOCO DE CÓDIGO
@app.route("/projeto1")
def projeto1():
    return render_template("projeto1.html")