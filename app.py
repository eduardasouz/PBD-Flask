from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>olá <br> Mundo!</h1>"


@app.route("/aluno/<nome>")
def aluno(nome):
    return render_template('aluno.html')