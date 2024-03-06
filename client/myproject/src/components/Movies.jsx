import React, { useState } from 'react'
import { useSelector } from 'react-redux'
import { Link, useParams } from 'react-router-dom'
import Movie from './Movie'


export default function Movies() {

    const [finalMovies, setFinalMovies] = useState([])

    const movies = useSelector((store) => store.movies)

    const params = useParams()
    // console.log(params.id);

    const searchMovies = (e) => {
        const filteredMovies = movies?.filter((movie) => movie.name.toLowerCase().includes(e.toLowerCase()))
        setFinalMovies(filteredMovies)
        // console.log(finalMovies)
    }

    return (
        <div>

            <br></br>

            <div>

                search <input type='text' onChange={(e) => { searchMovies(e.target.value) }} />

                <br></br><br></br>

                <Link to={'/mainPage/addMovie'}><button >Add Movie</button><br></br></Link>

                {(finalMovies.length > 0 ? finalMovies : movies)?.map((movie) => <Movie key={movie._id} movieData={movie} />).reverse()}

            </div>

        </div>
    )
}

