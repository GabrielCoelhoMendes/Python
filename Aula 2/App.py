from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    dados = {
        "nome": "Gabriel Coelho Mendes",
        "cargo": "Estudante",
        "email": "email@exemplo.com",
        "telefone": "(31) 99999-9999",
        "github": "github.com/GabrielCoelhoMendes/",

        "habilidades": [
            "Python",
            "Flask",
            "SQL",
            "Html, Css, Javascript"
        ]
    }

    return render_template("index.html", dados=dados)

if __name__ == "__main__":
    app.run(debug=True)