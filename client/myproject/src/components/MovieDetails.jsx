import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link, useNavigate, useParams } from 'react-router-dom';

import { addItem, updateItem } from '../utils';

export default function MovieDetails(props) {
    const [movie, setMovie] = useState({});

    const params = useParams();
    const navigate = useNavigate()
    const dispatch = useDispatch()

    //add movie
    const addMovie = async (event) => {
        event.preventDefault(); // Prevent default form submission

        const newMovie = await addItem("http://127.0.0.1:5000/subscriptions/movies", movie);

        // Dispatch action to update movies list in Redux store
        dispatch({ type: "ADD_MOVIE", payload: newMovie });

        alert(`The new movie "${newMovie.name}" created successfully`);

        navigate('/mainPage/movies')
        // console.log(newMovie);
    };

    //update movie
    const movieToUpdate = useSelector((store) => store.movies?.find((m) => m._id == params.id));

    const updateMovie = async (event) => {
        event.preventDefault(); // Prevent default form submission

        console.log(movie);
        const updatedMovie = await updateItem(`http://127.0.0.1:5000/subscriptions/movies/${movieToUpdate._id}`, movie);
        console.log(updatedMovie);

        // Dispatch action to update movies list in Redux store
        dispatch({ type: "UPDATE_MOVIE", payload: updatedMovie });

        alert(`The movie with ID "${updatedMovie._id}" updated successfully`);

        navigate('/mainPage/movies')
    };


    return (
        <div>
            {props.addMovie ? <h2>New Movie: </h2> : <h2>Edit Movie "{movieToUpdate?.name}" </h2>}

            <form onSubmit={props.addMovie ? addMovie : updateMovie}>

                <div>
                    Name: <input type="text" required
                        defaultValue={props.editMovie ? movieToUpdate?.name : ''}
                        onChange={(e => setMovie({ ...movie, name: e.target.value }))} />
                    <br></br>
                    Genres: <input type="text" required
                        defaultValue={props.editMovie ? movieToUpdate?.genres : ''}
                        onChange={(e => setMovie({ ...movie, genres: e.target.value }))} />
                    <br></br>
                    Image url: <input type="text" required
                        defaultValue={props.editMovie ? movieToUpdate?.image : ''}
                        onChange={(e => setMovie({ ...movie, image: e.target.value }))} />
                    <br></br>
                    Premiered: <input type="text" required
                        defaultValue={props.editMovie ? movieToUpdate?.premiered : ''}
                        onChange={(e => setMovie({ ...movie, premiered: e.target.value }))} />
                    <br></br><br></br>
                </div>

                {props.addMovie ? <button type="submit">Save</button> : <button type="submit">Update</button>}

                <Link to={'/mainPage/movies'}><button >Cancel</button></Link>

            </form>
        </div>
    );
}
