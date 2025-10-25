# Desafio Técnico Backend

## Resumo 

Essa é minha solução adaptada do desafio técnico compartilhado no [LinkedIn](https://www.linkedin.com/posts/d3vlopes_desafio-t%C3%A9cnico-backend-ugcPost-7386898997443178496-h03d?utm_source=social_share_send&utm_medium=android_app&rcm=ACoAACJ5cskBSGZnF8oggBgEcQjmUZi9B7Pzcr4&utm_campaign=share_via)

## Objetivo

Nesse desafio, você deve construir um sistema de enquetes em realtime, permitindo que os usuários criem enquetes com perguntas de múltipla escolha.


## Diagrama do DB


<img src="assets/images/er_diagram.png" alt="Diagrama do DB" width=300 style="display:block; margin:auto;">


## Requisitos

- Deve ser possível criar uma enquete
- Deve ser possível editar uma enquete
- Deve ser possível excluir uma enquete
- Deve ser possível listar todas as enquetes
- Deve ser possível listar as enquetes por status
- Deve ser possível adicionar opções ilimitadas na enquete
- Deve ser atualizado o número de votos sem precisar atualizar a página (realtime)
- Deve conter teste de todos os controllers

## Stacks (adaptada)

- Python
- SQLAlchemy
- FastAPI
- Pydantic
- Pytest
- PostgreSQL
- Docker
- Swagger

## Regras de Negócio

- A enquete deve ter uma pergunta
- A enquete deve ter uma data de início
- A enquete deve ter uma data de término
- A enquete pode ter o status não iniciado/iniciado/em andamento/finalizado
- A enquete deve ter no mínimo 3 opções
- A enquete não pode ser editada depois de iniciar


# Rastreabilidade de Requisitos

| ID    | Requisito                                                      | Teste                          | Arquivo            |
|-------|----------------------------------------------------------------|----------------------------------------------|----------------------------|
| RQ01  | Deve ser possível criar uma enquete                             | test_create_poll                              | tests/test_polls.py        |
| RQ02  | Deve ser possível editar uma enquete                             | test_edit_poll                                | tests/test_polls.py        |
| RQ03  | Deve ser possível excluir uma enquete                            | test_delete_poll                              | tests/test_polls.py        |
| RQ04  | Deve ser possível listar todas as enquetes                       | test_list_all_polls                           | tests/test_polls_list.py   |
| RQ05  | Deve ser possível listar as enquetes por status                  | test_list_polls_by_status                     | tests/test_polls_list.py   |
| RQ06  | Deve ser possível adicionar opções ilimitadas na enquete         | test_add_unlimited_options                     | tests/test_options.py      |
| RQ07  | Deve ser atualizado o número de votos sem precisar atualizar a página (realtime) | test_realtime_vote_update                      | tests/test_votes.py        |
| RQ08  | Deve conter teste de todos os controllers                        | test_controllers_coverage                      | tests/test_controllers.py  |
