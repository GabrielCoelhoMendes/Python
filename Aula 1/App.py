# Importa a classe Flask da biblioteca flask
from flask import Flask

# Cria a aplicação Flask
app = Flask(__name__)

# Decorator que define a rota "/decorator"
# Quando alguém acessar essa URL no navegador,
# a função abaixo será executada
@app.route('/')
def explicar_decorator():

    # Retorna um conteúdo HTML exibido no navegador
    return """
    <h1>Decorators em Python</h1>

    <h2>O que é um decorator?</h2>
    <p>
    Um decorator em Python é uma função que modifica o comportamento
    de outra função sem alterar diretamente seu código.
    </p>

    <h2>Para que serve?</h2>
    <p>
    Decorators ajudam a reutilizar código e adicionar funcionalidades
    extras, como autenticação, logs e validações.
    </p>

    <h2>Como é utilizado no Flask?</h2>
    <p>
    No Flask, decorators são usados para criar rotas.
    Exemplo:
    </p>

    <pre>
    @app.route('/')
    def home():
        return "Página inicial"
    </pre>

    <p>
    O decorator @app.route associa uma função a uma URL.
    Quando a URL é acessada, a função correspondente é executada.
    </p>

    <p>
    ૮꒰ ˶• ༝ •˶꒱ა ♡
    </p>
    """

# Verifica se o arquivo está sendo executado diretamente
# (e não importado em outro arquivo)
if __name__ == '__main__':

    # Inicia o servidor Flask
    # debug=True faz o servidor reiniciar automaticamente
    # quando houver alterações no código
    app.run(debug=True)