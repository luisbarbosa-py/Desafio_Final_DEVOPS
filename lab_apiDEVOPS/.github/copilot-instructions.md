## Instruções rápidas para agentes AI (Português)

Este repositório contém uma API Flask simples usada para demonstração/treinamento. O objetivo deste arquivo é dar ao agente contexto prático e exemplos concretos para ser produtivo ao editar, testar e estender este projeto.

Pontos principais (visão geral)

- A aplicação principal está em `app.py`. É uma API Flask com rotas: `/` (status), `/items` (lista estática), `/login` (gera JWT) e `/protected` (rota protegida por JWT).
- A documentação Swagger está em `static/swagger.json` e montada em `/swagger` via `flask_swagger_ui`.
- Testes simples usando `unittest` estão em `teste_app.py` e esperam comportamento padrão das rotas.

Comandos úteis / fluxo de desenvolvimento

- Executar localmente (venv):
  - Instalar dependências: `pip install -r requirements.txt`
  - Rodar: `python app.py` (escuta em 0.0.0.0:1313)
- Docker:
  - Build: `docker build -t lab_api .`
  - Rodar com docker-compose: `docker compose up --build` (mapeia 1313)
- Testes:
  - Executar: `python -m unittest teste_app.py` ou `python teste_app.py`

Padrões e convenções do projeto

- Estrutura enxuta: todo o código da API vive em `app.py` (sem pacotes separados). Ao estender, prefira criar módulos sob um diretório `src/` ou `app/` e mantenha as rotas registradas via Blueprints.
- JWT: a chave está em `app.config['JWT_SECRET_KEY'] = 'your_secret_key'`. Em commits reais, substitua por segredos seguros e variabilize com `FLASK_ENV`/variáveis de ambiente.
- Testes: `teste_app.py` usa `app.test_client()`; ao adicionar testes, siga o padrão `unittest` e mantenha a compatibilidade sem rodar o servidor real.

Padrões detectáveis no código (exemplos)

- Geração de token (exemplo):
  - `access_token = create_access_token(identity="user")` em `app.py` — tokens sem payload extra.
- Proteção de rota:
  - Decorador `@jwt_required()` usado em `/protected`.
- Swagger:
  - UI montada via `get_swaggerui_blueprint(SWAGGER_URL, API_DOC_URL)` e registrada com `app.register_blueprint(...)`.

Integrações e pontos de atenção

- Dependências listadas em `requirements.txt` (versões fixas para Flask e extensões). Ao atualizar Werkzeug, alguns testes podem falhar; `teste_app.py` aplica um patch temporário para `werkzeug.__version__` — preserve essa estratégia se atualizar dependências.
- Docker/HMR: `docker-compose.yml` monta o diretório (`.:/app`) para desenvolvimento. Tenha cuidado com comportamento de caches entre host/contêiner ao editar arquivos.

O que o agente deve priorizar ao editar o repositório

1. Preservar as rotas existentes e a compatibilidade dos testes. Antes de alterar respostas, atualize `teste_app.py`.
2. Mantener a documentação Swagger sincronizada com as rotas (arquivo `static/swagger.json`).
3. Ao adicionar segredos, use variáveis de ambiente e atualize `Dockerfile`/`docker-compose.yml` conforme necessário.

Exemplos rápidos para mudanças comuns

- Adicionar uma rota GET com JSON:
  - Editar `app.py` e adicionar `@app.route('/nova', methods=['GET'])` retornando `jsonify(...)`.
- Criar Blueprint:
  - Criar pasta `app/` com `routes.py`, definir `bp = Blueprint('..', __name__)` e `app.register_blueprint(bp)` em `app.py`.

Notas finais

- Este arquivo foca apenas em padrões observáveis no código. Se precisar de convenções de estilo (formatadores, linting) ou CI, peça detalhes e eu adiciono se esses arquivos existirem.

Se algo estiver incorreto ou faltando detalhes específicos do fluxo local, confirme e eu ajusto o conteúdo.
