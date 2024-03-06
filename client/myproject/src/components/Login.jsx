import React from 'react'
import { Link } from 'react-router-dom'

export default function Login() {
  return (
    <div>
      <h2>Login</h2>

      <h3>User Name</h3><input type='text' />
      <h3>Password</h3><input type='text' />

      <br></br><br></br>

      <button>Login</button>

      <br></br><br></br>

      <h4>New User ?</h4>
      <Link to="/createAccount">Create Account</Link>


    </div>
  )
}
