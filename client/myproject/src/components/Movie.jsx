import React from 'react'
import { Link, useNavigate } from 'react-router-dom'

import { deleteItem } from '../utils'
import { useDispatch } from 'react-redux'
import Subscriptions from './Subscriptions'


export default function Movie({ movieData }) {

    const dispatch = useDispatch()
    const navigate = useNavigate()

    //delete movie
    const deleteMovie = async () => {

        await deleteItem(`http://127.0.0.1:5000/subscriptions/movies/${movieData._id}`)


        dispatch({ type: "DELETE_MOVIE", payload: movieData._id });

        alert(`The movie "${movieData.name}" deleted successfully`);
        navigate('/mainPage/movies')
    }

    return (
        <div className='movieCard'>

            <h2>{movieData.name}</h2>
            <h3>{movieData.premiered}</h3>
            <h4>Geners: {movieData.genres?.map((g) => `${g}, `)}</h4>
            <img src={movieData.image} style={{ width: '100px', height: "150px" }} />
            <br></br>

            <Link to={`/mainPage/editMovie/${movieData._id}`}><button>Edit</button></Link>&nbsp;
            <button onClick={deleteMovie}>Delete</button>

            <Subscriptions movieId={movieData._id} />


        </div>
    )
}
