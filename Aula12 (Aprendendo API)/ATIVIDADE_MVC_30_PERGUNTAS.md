# Atividade Aula 12 — Model, Controller e View (StreamFlix)

**Disciplina:** Python / Flask  
**Profª:** Janaína Duarte  
**Projeto:** `flask/Aula12/`  
**Objetivo:** Explorar o código, localizar arquivos e explicar o que cada camada faz.

---

## Como responder

1. Abra a pasta `flask/Aula12/` no editor ou GitHub.
2. Navegue pelas pastas `models/`, `controllers/` e `views/`.
3. Rode o site (`python app.py`) quando a pergunta pedir para testar no navegador.
4. Responda com **caminho do arquivo** + **explicação em suas palavras**.

**Identificação**

- Nome: Gabriel Coelho Mendes
- Turma: 3B1

---

## Bloco A — Model (perguntas 1 a 10)

**1.** Em qual pasta ficam as classes que representam tabelas do banco SQLite? Cite o caminho.

        H:\2 - PYTHON\2 Etapa\Aula12 (Aprendendo API)\models 

**2.** Qual é o nome do arquivo de banco criado quando o app roda? Em qual arquivo Python essa configuração está?

        streamflix.db   /  no app.py

**3.** Quais classes Model existem no projeto (nome das classes)? Em quais arquivos `.py` cada uma está?

        ModeloBase...             ❁✿❀-`♡´-❀✿❁          ...models/base.py
        FilmeFavorito...          ❁✿❀-`♡´-❀✿❁          ...models/filme_favorito.py
        HistoricoBusca...         ❁✿❀-`♡´-❀✿❁          ...models/historico_busca.py

**4.** De qual superclasse `FilmeFavorito` e `HistoricoBusca` herdam? O que elas ganham automaticamente por herança (cite 3 campos)?

        Do "ModeloBase"    /    id, data_criacao, data_atualizacao

**5.** Qual é o `__tablename__` da tabela de favoritos? Por que usamos `__tablename__` em vez de só o nome da classe?

        "filmes_favoritos"    /    para deixar o código desconectado, permitir o nome que quiser e evitar conflitos com restrições de bancos de dados.

**6.** No model `FilmeFavorito`, qual coluna guarda o id do filme vindo da API TMDB? Ela tem alguma restrição especial (`unique`, `nullable`)?

        tmdb_id    /    sim, nullable=False e unique=True

**7.** Abra `models/filme_favorito.py`. O que o método `@classmethod adicionar` faz passo a passo? O que acontece se o filme já existir nos favoritos?

        como o nome sugeri, ele adiciona um filme no banco de dados de favoritos   /    Se o filme já estiver cadastrado, o método interrompe a execução imediatamente e retorna None

**8.** Onde está o método que lista as últimas 8 buscas? Qual é o nome da classe e do método?

        models/historico_busca.py   /    ultimas , ultimas

**9.** O model grava dados da API TMDB inteira ou só alguns campos espelhados? Cite 4 campos salvos em `FilmeFavorito`.

        só alguns campos espelhados   /    tmdb_id, titulo, poster_path, nota, ano

**10.** Em `models/__init__.py`, o que é exportado além de `db`? Por que o controller importa `from models import FilmeFavorito` em vez de importar o arquivo inteiro da pasta?

        "ModeloBase", "FilmeFavorito", "HistoricoBusca"   /    salvar espaço, só pegando o a classe necessária invés da pag toda
---

## Bloco B — Controller (perguntas 11 a 20)

**11.** Quantos Blueprints existem no projeto? Cite o **nome** de cada um e o **url_prefix** (se tiver).

        3 blueprints   /   dashboard_bp  , favoritos_bp e /favoritos , filmes_bp e /filmes

**12.** Em qual arquivo está a rota `/filmes/populares`? Qual é o nome da função Python que responde essa URL?

        ontrollers\filmes_controller.py   /   populares

**13.** O que a função `populares()` faz antes de chamar `render_template`? Cite duas chamadas (Model, Service ou API).

        Chama a api e chama o model  /   TmdbApi.filmes_populares() e FilmeFavorito.listar()

**14.** Quando o usuário busca um filme em `/filmes/buscar`, qual controller registra o termo no banco? Qual model é usado e em qual linha aproximada?
        Controller: controllers/filmes_controller.py
        Model: HistoricoBusca
        Linha aproximada: 50, na chamada HistoricoBusca.registrar(termo, len(filmes))
        
**15.** Abra `controllers/favoritos_controller.py`. Qual método HTTP é exigido para adicionar favorito (`GET` ou `POST`)? Qual a URL completa de exemplo para adicionar o filme id 550?
        Método: POST
        URL: /favoritos/adicionar/550

**16.** No `filmes_controller.py`, rota `detalhe(filme_id)`: o que acontece se `api.detalhe(filme_id)` retornar `None`?
        O usuário é redirecionado para a página de filmes populares usando redirect(url_for("filmes.populares")).
        

**17.** Onde os Blueprints são **registrados** no Flask? Cite o arquivo e o comando usado (3 registros).
        app.register_blueprint(dashboard_bp)
        app.register_blueprint(filmes_bp)
        app.register_blueprint(favoritos_bp)
        

**18.** Qual controller cuida da página inicial `/`? Quais variáveis ele envia para o template `index.html`?
        controller: controllers/dashboard_controller.py   I    populares, melhores, total_favoritos, historico, modo_demo

**19.** A pasta `services/tmdb_api.py` é Model, Controller ou View? Justifique: quem chama essa classe e para quê?
        Não é nenhuma das três camadas. Ela pertence à camada Service. Os controllers chamam a classe TmdbApi para buscar informações da API do TMDB sem colocar essa lógica dentro dos controllers.

**20.** No controller de busca, de onde vem o termo digitado quando o usuário usa o formulário da home (`index.html`)? É `request.form` ou `request.args`? Explique a diferença nesse projeto.
        Pode vir dos dois:
        
        request.args quando a busca é feita por GET.
        request.form quando é enviada por POST.
        
        Neste projeto o controller verifica primeiro request.args e, se o método for POST, usa request.form.
---

## Bloco C — View (perguntas 21 a 30)

**21.** Onde ficam os templates HTML? Qual caminho completo da pasta?
        views/templates/

**22.** Qual template é a “base” de todas as páginas (layout com menu)? Como os outros templates usam esse layout (qual comando Jinja)?
        Arquivo: views/templates/layout.html   I   {% extends "layout.html" %}

**23.** Abra `views/templates/layout.html`. Liste os 5 links do menu e o `url_for` de cada um.
        StreamFlix       →      url_for('dashboard.index')
        Populares        →      url_for('filmes.populares')
        Melhores         →      url_for('filmes.melhores')
        Buscar           →      url_for('filmes.buscar')
        Favoritos        →      url_for('favoritos.listar')

**24.** Qual arquivo HTML exibe a seção **“Onde assistir (Brasil)”**? De onde vem a variável `streaming` usada nessa tela?
        views/templates/filmes/detalhe.html   I   do controller controllers/filmes_controller.py, através da chamada:streaming, demo = api.streaming(filme_id)

**25.** O arquivo `filmes/_card.html` é uma página inteira ou um pedaço reutilizado? Quem inclui esse arquivo e com qual tag Jinja?
        pedaço reutilizado   I   {% include "filmes/_card.html" %}

**26.** Em `filmes/detalhe.html`, como a View sabe se o filme já está nos favoritos? Qual variável booleana/objeto controla o botão “Salvar” vs “Remover”?
        Pela variável favorito.
        Se ela existir, mostra Remover dos favoritos.
        Caso contrário, mostra Salvar favorito.

**27.** Onde está o CSS do site? Como o `layout.html` carrega esse arquivo (função Flask/Jinja)?
        views/static/css/style.css   I   { url_for('static', filename='css/style.css') }}

**28.** Na listagem de favoritos (`favoritos/lista.html`), qual loop Jinja percorre os registros? Cite 3 campos exibidos na tabela.
        {% for fav in favoritos %}   I   fav.titulo, fav.nota, fav.ano

**29.** O que significa `{% if modo_demo %}` no layout? Quem disponibiliza essa variável para **todos** os templates?
        Significa que será exibido um aviso quando o sistema estiver funcionando em modo demonstração (sem chave da API TMDB).
        Essa variável é disponibilizada para todos os templates pelo context_processor definido em app.py 

**30.** Desenhe ou descreva o fluxo completo quando o aluno clica em **“Salvar favorito”** no detalhe do filme, indicando **View → Controller → Model** (e redirect de volta). Cite arquivos envolvidos.
        O usuário clica em Salvar favorito na página views/templates/filmes/detalhe.html.
        O formulário envia um POST para /favoritos/adicionar/<tmdb_id>.
        A rota é tratada em controllers/favoritos_controller.py, função adicionar().
        O controller coleta os dados do formulário e chama FilmeFavorito.adicionar().
        O model models/filme_favorito.py salva o filme no banco SQLite.
        Após salvar, o controller faz redirect() para a página anterior (voltar), retornando ao detalhe do filme.
---

## Entrega

- Arquivo `.txt` ou `.md` com as 30 respostas 

**Critério:** respostas que mostrem que você **abriu o código**, não chute.

Boa exploração!
