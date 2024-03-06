import './App.css'

import { useDispatch } from 'react-redux'
import { useEffect, useState } from 'react'

import HomePage from './components/HomePage'

import { getAll } from './utils'

function App() {

  const dispatch = useDispatch()

  useEffect(() => {

    const getAllData = async () => {
      const users = await getAll("http://localhost:5000/users")
      const movies = await getAll("http://127.0.0.1:5000/subscriptions/movies")
      const members = await getAll("http://127.0.0.1:5000/subscriptions/members")
      const subscriptions = await getAll("http://127.0.0.1:5000/subscriptions/subscriptions")

      dispatch({ type: "LOAD", payload: { users, movies, members, subscriptions } })

    }

    getAllData()

  }, [])



  return (
    <>
      <HomePage />
    </>
  )
}

export default App
