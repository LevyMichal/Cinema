const express = require('express')
const router = express.Router();

const moviesBLL = require("../BLL/moviesBLL")

router.route('/').get(async (req, res) => {
    const movies = await moviesBLL.getAllMovies();
    res.json(movies);
});

router.route('/:id').get(async (req, res) => {
    const { id } = req.params;
    const movie = await moviesBLL.getMovieById(id);
    res.json(movie);
});

router.route('/').post(async (req, res) => {
    const newMovie = req.body;
    const result = await moviesBLL.addMovie(newMovie);
    res.json(result);
});

router.route('/:id').put(async (req, res) => {
    const { id } = req.params;
    const updatedMovie = req.body;
    const result = await moviesBLL.updateMovie(id, updatedMovie)
    res.json(result)
})

router.route('/:id').delete(async (req, res) => {
    const { id } = req.params;
    const result = await moviesBLL.deleteMovie(id);
    res.json(result)
});

module.exports = router;