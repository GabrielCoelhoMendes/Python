from flask import Blueprint, redirect, render_template, request, url_for

from models import Colecionador, Figurinha, ItemOferta, OfertaTroca, db

figurinhas_bp = Blueprint("figurinhas", __name__, url_prefix="/figurinhas")


@figurinhas_bp.route("/")
def index():
    ofertas = OfertaTroca.listar_com_colecionador()
    return render_template("figurinhas/lista_ofertas.html", ofertas=ofertas)


@figurinhas_bp.route("/oferta/cadastrar", methods=["GET", "POST"])
def cadastrar_oferta():
    colecionadores = Colecionador.listar()
    figurinhas = Figurinha.listar()
    
    if request.method == "POST":
        # 1. Captura os dados do formulário enviado (exemplo genérico)
        colecionador_id = request.form.get("colecionador_id")
        figurinha_oferecida_id = request.form.get("figurinha_oferece_id")
        figurinha_desejada_id = request.form.get("figurinha_deseja_id")
        observacao = request.form.get("observacao")
        # 2. Cria a nova oferta de troca
        nova_oferta = OfertaTroca.criar(
        colecionador_id=colecionador_id,
        observacao=observacao
)
        
        # 3. Cria os itens da oferta (o que oferece e o que deseja)
        ItemOferta.criar(oferta_id=nova_oferta.id, figurinha_id=figurinha_oferecida_id, tipo="oferece")
        ItemOferta.criar(oferta_id=nova_oferta.id, figurinha_id=figurinha_desejada_id, tipo="deseja")
        
        # 4. Redireciona para a listagem após o cadastro com sucesso
        return redirect(url_for("figurinhas.index"))
        
    return render_template(
        "figurinhas/formulario_oferta.html",
        colecionadores=colecionadores,
        figurinhas=figurinhas,
    )