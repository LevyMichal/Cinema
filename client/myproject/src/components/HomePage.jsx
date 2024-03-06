import React from 'react'
import { Router, Routes, Route } from 'react-router-dom'

import CreateAccount from './CreateAccount'
import Login from './Login'
import MainPage from './MainPage'
import Movies from './Movies'
import Members from './Members'
import Users from './Users'
import Details from './Details'

export default function HomePage() {
  return (
    <div>
      <Routes>
        <Route path="" element={<Login />} />
        <Route path={'/createAccount'} element={<CreateAccount />} />

        <Route path={'/mainPage'} element={<MainPage />} >

          <Route path={'movies'} element={<Movies />} />
          <Route path={"addMovie"} element={<Details addMovie={true} />} />
          <Route path={'editMovie/:id'} element={<Details editMovie={true} />} />

          <Route path={'subscriptions/members'} element={<Members />} />
          <Route path={"addMember"} element={<Details addMember={true} />} />
          <Route path={'editMember/:id'} element={<Details editMember={true} />} />

          <Route path={'users'} element={<Users />} />
          <Route path={"addUser"} element={<Details addUser={true} />} />
          <Route path={'editUser/:id'} element={<Details editUser={true} />} />

        </Route >

      </Routes >
    </div >
  )
}
