const mongoose = require('mongoose')

const MemberSchema = new mongoose.Schema({
    name: { type: String },
    email: { type: String },
    city: { type: String }
}, { versionKey: false })

module.exports = mongoose.model('member', MemberSchema)