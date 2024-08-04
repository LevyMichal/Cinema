import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Link, Outlet } from 'react-router-dom'
import { get } from '../utils'

import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';



export default function MainPage() {

    const pages = ['Movies', 'Subscriptions', 'User Management'];
    const links = ["Movies", "members", "Users"]


    const user = useSelector((store) => store.user)

    const dispatch = useDispatch()

    useEffect(() => {
        const getAllData = async () => {
            const movies = await get("http://127.0.0.1:5000/subscriptions/movies")
            const members = await get("http://127.0.0.1:5000/subscriptions/members")
            const subscriptions = await get("http://127.0.0.1:5000/subscriptions/subscriptions")

            if (user.userName === "admin@gmail.com") {
                const users = await get("http://localhost:5000/users");
                dispatch({ type: "LOAD", payload: { movies, members, subscriptions, users } });

            } else {
                dispatch({ type: "LOAD", payload: { movies, members, subscriptions } });
            }
        };

        getAllData()

    }, [])



    return (
        <div>

            <Box sx={{ flexGrow: 1 }}>
                <AppBar position="static">
                    <Toolbar>
                        <Typography variant="h6"
                            // noWrap
                            component="a"
                            href="#app-bar-with-responsive-menu"
                            sx={{
                                mr: 2,
                                // display: { xs: 'none', md: 'flex' },
                                fontFamily: 'monospace',
                                fontWeight: 700,
                                letterSpacing: '.3rem',
                                color: 'inherit',
                                textDecoration: 'none',
                            }}
                        >
                            {pages.map((page, i) => <Link variant='inherit' to={links[i]}><Button variant="h6" component="div" sx={{ flexGrow: 1 }}>

                                {page}

                            </Button> </Link>)}

                            <Button color="inherit">
                                <Link to={"/"}>Logout</Link>
                            </Button>
                        </Typography>
                    </Toolbar>
                </AppBar>
            </Box>


            {/* <nav>
                
                <ul className='navbar'>
                    <li><Link className='link' to={'movies'}>Movies </Link></li>
                    <li><Link className='link' to={'members'}>Subscriptions </Link></li>
                    {user?.userName === "admin@gmail.com"
                        ? <li><Link className='link' to={'users'}>User Management </Link></li>
                        : null}
                    <li className='link'>{user.firstName} &nbsp;{user.lastName} </li>
                    <li><Link className='link' to={"/"}>Log Out </Link></li>
                </ul>
            </nav> */}

            <Outlet />

        </div >
    )
}
