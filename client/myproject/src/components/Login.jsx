import React, { useEffect, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { get } from '../utils'
import { useDispatch } from 'react-redux'
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Alert from '@mui/material/Alert';


// import AccountCircle from '@mui/icons-material/AccountCircle';

export default function Login() {

  const navigate = useNavigate()
  const dispatch = useDispatch()

  const [user, setUser] = useState({})
  const [loginError, setLoginError] = useState(false)

  const login = async (event) => {
    event.preventDefault()
    // console.log(user)

    const userExists = await get(`http://127.0.0.1:5000/users/username/${user.userName}`)
    // console.log(userExists)

    if (userExists && userExists.password === user.password) {
      const userLoggedIn = await get(`http://127.0.0.1:5000/users/${userExists._id}`)

      dispatch({ type: "USER", payload: userLoggedIn })

      navigate("/mainPage")
    } else {
      setLoginError(true)
    }
  }

  return (
    <div>
      <h2>Login</h2>

      <form>
        <Box sx={{ display: 'flex', alignItems: 'flex-end' }}>
          {/* <AccountCircle sx={{ color: 'action.active', mr: 1, my: 0.5 }} /> */}
          <TextField id="input-with-sx" label="UserName" variant="standard" required onChange={e => setUser({ ...user, userName: e.target.value })} />
        </Box>
        <br></br>
        <Box sx={{ display: 'flex', alignItems: 'flex-end' }}>
          {/* <AccountCircle sx={{ color: 'action.active', mr: 1, my: 0.5 }} /> */}
          <TextField id="input-with-sx" label="Password" variant="standard" required onChange={e => {
            setLoginError(false)
            setUser({ ...user, password: e.target.value })
          }} />
        </Box>

        <br></br>
        {loginError ? <Alert severity="error" variant="outlined">Username or Password is incorrect</Alert> : null}
        <br></br>

        <Button variant="contained" onClick={login}>Login</Button>

      </form>

      <br></br><br></br>
      {/*  */}
      <h4>New User ?</h4>
      <Link to="/createAccount">Create Password</Link>


    </div>
  )
}
