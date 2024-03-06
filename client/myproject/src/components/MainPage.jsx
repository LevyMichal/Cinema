import React from 'react'
import { Link, Outlet } from 'react-router-dom'
import Movies from './Movies'

export default function MainPage() {
    return (
        <div>

            <nav>
                <ul className='navbar'>
                    <li><Link className='link' to='movies'>Movies </Link></li>
                    <li><Link className='link' to='subscriptions/members'>Subscriptions </Link></li>
                    <li><Link className='link' to='users'>User Management </Link></li>
                </ul>
            </nav>

            <Outlet />

        </div>
    )
}
