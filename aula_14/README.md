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