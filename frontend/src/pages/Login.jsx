import '../styles/login.css'

function Login() {
  return (
    <div> 
      <h1>Pizzaria Login</h1>
      
      <form type="submit" action="#" method="POST">
        <label htmlFor="email">e-mail:</label>
        <input type="text" id="email" name="email" />

        <label htmlFor="pass">senha:</label>
        <input type="password" id="pass" name="pass" />

        <button type="submit">Entrar</button>
        <button type="button"> Criar nova conta </button>
      </form>
    </div>
  )
}

export default Login