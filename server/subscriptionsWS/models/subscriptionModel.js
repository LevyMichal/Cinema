
const mongoose = require('mongoose');

const SubscriptionSchema = new mongoose.Schema({
    memberId: { type: String },
    movies: [
        {
            movieId: { type: String },
            date: { type: String }
        }
    ]
}, {
    versionKey: false
});

module.exports = mongoose.model('subscription', SubscriptionSchema);