const mongoose = require("mongoose")

const MovieSchema = new mongoose.Schema({
    name: { type: String },
    genres: [],
    image: { type: String },
    premiered: { type: String }
}, { versionKey: false })

module.exports = mongoose.model("movie", MovieSchema)