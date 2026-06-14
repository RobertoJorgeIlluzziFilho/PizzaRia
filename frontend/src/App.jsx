
// o App.jsx é o gerenciador principal, ele decide:
// Qual página aparece?
// Qual rota aparece?
// Qual layout aparece?


// Rotas no REACT
import Home from './pages/Home'  // página após o usuário se autenticar
import Login from './pages/Login' // vai ser nossa "home" inicial
// import Cadastro from './pages/Cadastro'

function App() {
  return (
      <Login />
  )
}

// exportando nosso app pra fora
export default App