from app import app
from app.teste_dev import Licitacoes

from flask import render_template


@app.route('/')
def index():
    dados = Licitacoes.procura(self=app)
    quantidade = dados[0]
    valor = dados[1]
    return render_template('index.html', quantidade=quantidade, valor=valor)

