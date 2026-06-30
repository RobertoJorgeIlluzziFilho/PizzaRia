# 🍕 PizzaRia

Sistema web de pizzaria desenvolvido com React e Flask.

![Logo da PizzaRia](docs/logo.png)

---

## 📌 Sobre o projeto

A PizzaRia é uma aplicação fullstack focada em pedidos online de pizzas, desenvolvida para fins de estudo e prática em desenvolvimento web moderno.

O projeto utiliza:
- React no frontend
- Flask no backend
- Comunicação via API REST com JSON puro

---

## ✨ Funcionalidades

- 🔐 Sistema de login e cadastro de usuários
- 🍕 Visualização do cardápio de pizzas
- 📦 Criação e gerenciamento de pedidos (CRUD)
- ✏️ Edição e remoção de pedidos
- 📍 Busca automática de endereço via CEP (BrasilAPI)
- 🔒 Rotas protegidas com autenticação
- 📱 Interface responsiva
- ⚡ Integração frontend/backend via JSON

---

## 🛠️ Tecnologias utilizadas

### Frontend
- React 19
- Vite 8
- CSS puro (sem frameworks)
- JavaScript (ES Modules)
- React Router DOM v7

### Backend
- Flask (Python)
- Flask-CORS
- API REST
- JSON (arquivos como banco de dados)

---

## 📂 Estrutura do projeto

```bash
PizzaRia/
│
├── backend/                          ← Servidor Flask (API REST)
│   ├── app.py                        ← Inicialização do Flask + CORS + Blueprints
│   ├── requirements.txt              ← Dependências Python
│   ├── routes/
│   │   ├── auth.py                   ← POST /auth/login e /auth/register
│   │   ├── pedidos.py                ← CRUD /pedidos (GET, POST, DELETE, PATCH)
│   │   ├── pizzas.py                 ← GET /pizzas (cardápio)
│   │   └── user.py                   ← GET/PUT /user/perfil
│   └── data/
│       ├── usuarios.json             ← Base de usuários cadastrados
│       ├── pizzas.json               ← Cardápio de pizzas
│       ├── pedidos.json              ← Histórico de pedidos
│       └── enderecos.json            ← Endereços (reserva)
│
├── frontend/                         ← App React (Vite)
│   ├── index.html                    ← HTML principal (div#root)
│   ├── package.json                  ← Dependências (react, vite, react-router-dom)
│   ├── vite.config.js                ← Configuração do Vite
│   ├── eslint.config.js              ← Configuração do ESLint
│   ├── .gitignore                    ← Ignorar node_modules, dist, etc.
│   ├── README.md                     ← Documentação do frontend
│   ├── package-lock.json             ← Lock de versões das dependências
│   └── src/
│       ├── main.jsx                  ← Ponto de entrada React
│       ├── App.jsx                   ← Roteamento (BrowserRouter + todas as rotas)
│       ├── services/
│       │   └── api.js                ← Central de chamadas HTTP ao backend
│       ├── pages/
│       │   ├── Login.jsx             ← Tela de login
│       │   ├── Cadastro.jsx          ← Tela de cadastro
│       │   ├── Home.jsx              ← Dashboard inicial (stats + pizzas + pedidos)
│       │   ├── Cardapio.jsx          ← Cardápio completo de pizzas
│       │   ├── NovoPedido.jsx        ← Wizard de montagem + checkout
│       │   ├── MeusPedidos.jsx       ← Lista de pedidos + filtros + timers
│       │   └── Perfil.jsx            ← Editar dados pessoais + endereço
│       ├── components/
│       │   ├── AuthLayout.jsx        ← Layout visual da tela de login (split)
│       │   ├── AuthForm.jsx          ← Formulário reutilizável login/cadastro
│       │   ├── DashboardLayout.jsx   ← Layout com sidebar + conteúdo
│       │   ├── Navbar.jsx            ← Sidebar de navegação
│       │   ├── ProtectedRoute.jsx    ← Guardião de rotas (redireciona se não logado)
│       │   ├── PizzaCard.jsx         ← Card individual de pizza
│       │   ├── PizzaSelector.jsx     ← Seletor de sabor no wizard
│       │   ├── SizeSelector.jsx      ← Seletor de tamanho
│       │   ├── ExtrasSelector.jsx    ← Seleção de adicionais
│       │   ├── OrderSummary.jsx      ← Resumo do pedido no carrinho
│       │   
│       │   
│       ├── styles/
│       │   ├── global.css            ← Reset básico e variáveis CSS
│       │   ├── login.css             ← Layout split da tela de login
│       │   ├── forms.css             ← Inputs, botões, grids de endereço
│       │   ├── dashboard.css         ← Layout dashboard (sidebar + content)
│       │   ├── navbar.css            ← Estilos da sidebar
│       │   ├── home.css              ← Home, stats, tabelas, pizza-grid
│       │   ├── card.css              ← Cards de pizza no cardápio
│       │   └── novo-pedido.css       ← Wizard de montagem e checkout
│       └── assets/
│           ├── background.png        ← Fundo da tela de login
│           ├── background_limpo.png  ← Fundo limpo
│           ├── logo.png              ← Logo principal
│           ├── logo_fundo_removido.png ← Logo sem fundo
│           ├── pizza-hero.png        ← Imagem hero da pizza
│           └── superior-esquerdo.png ← Imagem decorativa
│
├── docs/                             ← Documentação e assets extras
│   ├── logo.png                      ← Logo para o README
│   ├── logo_fundo_removido.png       ← Logo sem fundo
│   ├── logo_limpa.png                ← Logo limpa
│   
│
├── .github/
│   └── workflows/
│       └── sync-branches.yml         ← GitHub Actions: sincroniza backend/ e frontend/ entre branches
│
├── README.md                         ← Este arquivo
├── .gitignore                        ← Arquivos ignorados pelo git (raiz)
└── LICENSE                           ← Licença do projeto
```

---

## 🚀 Como executar

### Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install Flask Flask-CORS
python app.py
```

O servidor roda em `http://127.0.0.1:5000`

### Frontend

```bash
cd frontend
npm install
npm run dev
```

O servidor de desenvolvimento roda em `http://127.0.0.1:5173`

---

## 🔗 Fluxo de comunicação

```
[Browser] → React (Vite, :5173) → fetch() → Flask (:5000) → JSON files
                                         ↕
                                   BrasilAPI (CEP público)
```

1. O React (Vite) serve as páginas em `localhost:5173`
2. As páginas chamam funções em `src/services/api.js`
3. `api.js` faz requisições `fetch()` para o Flask em `localhost:5000`
4. O Flask lê/escreve nos arquivos JSON e retorna os dados
5. O React renderiza os dados recebidos

---

## 👥 Integrantes

| Nome | Matrícula | Responsabilidade |
|------|-----------|-----------------|
| Gustavo | 2024012987 | Estilos CSS + Layouts Estruturais + Infraestrutura + Documentação |
| Maurício | 2024011139 | Páginas React + Componentes Visuais + Assets |
| Roberto | 2024007038 | Backend (Flask) + Service Layer (api.js) + Roteamento (App.jsx) |

---
