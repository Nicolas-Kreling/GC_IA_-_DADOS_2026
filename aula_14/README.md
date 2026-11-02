# Casa de Sucos - API

API feita com FastAPI para cadastrar sucos e calcular calorias e açúcar
usando os dados da API pública [Fruityvice](https://www.fruityvice.com/).
Os cálculos consideram 100 g de cada fruta. Os sucos ficam guardados em
memória, então somem quando a aplicação é reiniciada.

## Como rodar

```bash
cd aula_14
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac
pip install -r requirements.txt
uvicorn main:app --reload
```

Swagger: http://127.0.0.1:8000/docs

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/frutas/{nome}` | Consulta uma fruta (nome, calorias e açúcar) |
| POST | `/sucos` | Cadastra um suco e calcula os totais |
| GET | `/sucos` | Lista todos os sucos cadastrados |
| PUT | `/sucos/{id}` | Atualiza as frutas de um suco e recalcula os totais |

## Tratamento de erros

- Fruta não encontrada: **404** com mensagem amigável
- Suco não encontrado (PUT): **404**
- Lista de frutas vazia: **400**
- Fruityvice fora do ar: **503**

## Testes realizados no Swagger

### GET /frutas/banana (200)
```json
{
  "nome": "Banana",
  "calorias": 96,
  "acucar": 17.2
}
```

### POST /sucos (201)
Corpo enviado:
```json
{
  "nome": "Vitamina Tropical",
  "frutas": ["banana", "strawberry"],
  "tem_gosto_de": "Tamarindo"
}
```
Resposta:
```json
{
  "id": 1,
  "nome": "Vitamina Tropical",
  "frutas": ["banana", "strawberry"],
  "tem_gosto_de": "Tamarindo",
  "total_calorias": 125,
  "total_acucar": 22.6
}
```

### GET /sucos (200)
```json
[
  {
    "id": 1,
    "nome": "Vitamina Tropical",
    "frutas": ["banana", "strawberry"],
    "tem_gosto_de": "Tamarindo",
    "total_calorias": 125,
    "total_acucar": 22.6
  }
]
```

### PUT /sucos/1 (200)
Corpo enviado:
```json
{
  "frutas": ["banana", "apple"]
}
```
Resposta:
```json
{
  "id": 1,
  "nome": "Vitamina Tropical",
  "frutas": ["banana", "apple"],
  "tem_gosto_de": "Tamarindo",
  "total_calorias": 148,
  "total_acucar": 27.5
}
```

### GET /frutas/abacaxizinho (404)
```json
{
  "detail": "Fruta 'abacaxizinho' não encontrada. Tente o nome em inglês (ex: banana, strawberry)."
}
```