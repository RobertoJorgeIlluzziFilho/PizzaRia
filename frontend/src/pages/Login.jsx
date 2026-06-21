import '../styles/login.css'
import { useState } from "react" // adicionar e gerenciar estados

function Login() {

  // criando variáveis para guardar o que o usuário digitar
  const [email, setEmail] = useState(""); // [valor, função-altera-valor]
  const [senha, setSenha] = useState(""); // valor, função-altera-valor

  // função de login asíncrona (nosso evento, na aula: "e")
  async function handleLogin(event){

    
  }
 

export default Login