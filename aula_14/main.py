from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI(title="Casa de Sucos")

URL_FRUITYVICE = "https://www.fruityvice.com/api/fruit/"

# "banco de dados" em memória
sucos = []
proximo_id = 1


class SucoEntrada(BaseModel):
    nome: str
    frutas: list[str]
    tem_gosto_de: str


class SucoAtualizar(BaseModel):
    frutas: list[str]


def buscar_fruta(nome: str):
    """Consulta uma fruta na Fruityvice e devolve o JSON dela."""
    try:
        resposta = requests.get(URL_FRUITYVICE + nome.strip().lower(), timeout=10)
    except requests.RequestException:
        raise HTTPException(
            status_code=503,
            detail="Não foi possível acessar a API Fruityvice. Tente novamente mais tarde.",
        )

    if resposta.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail=f"Fruta '{nome}' não encontrada. Tente o nome em inglês (ex: banana, strawberry).",
        )

    if resposta.status_code != 200:
        raise HTTPException(status_code=502, detail="Erro ao consultar a API Fruityvice.")

    return resposta.json()


def calcular_totais(frutas: list[str]):
    """Soma calorias e açúcar considerando 100g de cada fruta."""
    if len(frutas) == 0:
        raise HTTPException(status_code=400, detail="Informe pelo menos uma fruta.")

    total_calorias = 0
    total_acucar = 0

    for nome in frutas:
        dados = buscar_fruta(nome)
        total_calorias += dados["nutritions"]["calories"]
        total_acucar += dados["nutritions"]["sugar"]

    return total_calorias, round(total_acucar, 2)


@app.get("/frutas/{nome}")
def consultar_fruta(nome: str):
    dados = buscar_fruta(nome)
    return {
        "nome": dados["name"],
        "calorias": dados["nutritions"]["calories"],
        "acucar": dados["nutritions"]["sugar"],
    }


@app.post("/sucos", status_code=201)
def cadastrar_suco(entrada: SucoEntrada):
    global proximo_id

    total_calorias, total_acucar = calcular_totais(entrada.frutas)

    suco = {
        "id": proximo_id,
        "nome": entrada.nome,
        "frutas": entrada.frutas,
        "tem_gosto_de": entrada.tem_gosto_de,
        "total_calorias": total_calorias,
        "total_acucar": total_acucar,
    }
    sucos.append(suco)
    proximo_id += 1

    return suco


@app.get("/sucos")
def listar_sucos():
    return sucos


@app.put("/sucos/{id}")
def atualizar_suco(id: int, entrada: SucoAtualizar):
    for suco in sucos:
        if suco["id"] == id:
            total_calorias, total_acucar = calcular_totais(entrada.frutas)
            suco["frutas"] = entrada.frutas
            suco["total_calorias"] = total_calorias
            suco["total_acucar"] = total_acucar
            return suco

    raise HTTPException(status_code=404, detail=f"Suco com id {id} não encontrado.")
