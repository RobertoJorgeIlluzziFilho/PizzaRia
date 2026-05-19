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
- 📍 Busca automática de endereço via CEP
- 🔒 Rotas protegidas com autenticação
- 📱 Interface responsiva
- ⚡ Integração frontend/backend via JSON
---

## 🛠️ Tecnologias utilizadas

### Frontend
- React
- Vite
- CSS puro
- JavaScript

### Backend
- Flask
- Flask-CORS
- API REST
- JSON

---

## 📂 Estrutura do projeto 

```bash
PizzaRia/
│
├── frontend/
│   │
│   ├── public/
│   │
│   ├── src/
│   │   │
│   │   ├── assets/
│   │   │   └── logo.png
│   │   │
│   │   ├── components/
│   │   │   ├── Navbar.jsx
│   │   │   ├── PizzaCard.jsx
│   │   │   └── PedidoCard.jsx
│   │   │
│   │   ├── pages/
│   │   │   ├── Login.jsx
│   │   │   ├── Cadastro.jsx
│   │   │   ├── Home.jsx
│   │   │   ├── NovoPedido.jsx
│   │   │   └── MeusPedidos.jsx
│   │   │
│   │   ├── services/
│   │   │   └── api.js
│   │   │
│   │   ├── styles/
│   │   │   ├── global.css
│   │   │   ├── navbar.css
│   │   │   ├── card.css
│   │   │   └── forms.css
│   │   │
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
├── backend/
│   │
│   ├── data/
│   │   ├── usuarios.json
│   │   └── pedidos.json
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   └── pedidos.py
│   │
│   ├
│   │   
│   │
│   ├── app.py
│   ├── requirements.txt
│   └── .env
│
├── docs/
│   └── logo.png
│
├── README.md
└── .gitignore
```

## 👥 Integrantes

- Gustavo   (n° 2024012987)
- Maurício  (n° matrícula)
- Roberto   (n° 2024007038)