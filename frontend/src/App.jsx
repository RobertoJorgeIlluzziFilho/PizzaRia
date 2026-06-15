// o App.jsx é o gerenciador principal, ele decide:
// Qual página aparece?
// Qual rota aparece?
// Qual layout aparece?

// Rotas no REACT
import { BrowserRouter, Routes, Route } from 'react-router-dom'

import Home from './pages/Home'   // página após autenticação
import Login from './pages/Login' // tela inicial
// import Cadastro from './pages/Cadastro'

// path principal, quando o usuário acessar a rota Root
// Ele irá redirecionar automaticamente pro /Login
function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Login />} />
        </Routes>
      </BrowserRouter>
    </div>
  )
}

// exportando nosso app pra fora
export default App