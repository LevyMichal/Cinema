const MovieModel = require("../models/movieModel")

//get all movies
async function getAllMovies() {
    const movies = await MovieModel.find({})
    return movies
}

//get movie by id
async function getMovieById(id) {
    const movie = await MovieModel.findById(id)
    return movie
}

//add movie
async function addMovie(movie) {
    const newMovie = new MovieModel(movie)
    await newMovie.save()
    return newMovie
}

//update movie
async function updateMovie(id, movie) {
    await MovieModel.findByIdAndUpdate(id, movie)
    const updatedMovie = getMovieById(id)
    // console.log(updatedMovie)
    return updatedMovie
}

//delete movie
async function deleteMovie(id) {
    await MovieModel.findByIdAndDelete(id)
    return `the movie whis ID ${id} DELETED`
}

module.exports = { getAllMovies, getMovieById, addMovie, updateMovie, deleteMovie }


