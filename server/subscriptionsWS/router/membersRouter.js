const express = require('express')
const router = express.Router();

const membersBLL = require("../BLL/membersBLL")

router.route('/').get(async (req, res) => {
    const members = await membersBLL.getAllMembers();
    res.json(members);
});

router.route("/:id").get(async (req, res) => {
    const { id } = req.params
    const member = await membersBLL.getMemberById(id)
    res.json(member)
})

router.route('/').post(async (req, res) => {
    const newMember = req.body
    const result = await membersBLL.addMember(newMember)
    res.json(result)
})

router.route('/:id').put(async (req, res) => {
    const { id } = req.params
    const updatedMember = req.body
    const result = await membersBLL.updateMember(id, updatedMember)
    res.json(result)
})

router.route('/:id').delete(async (req, res) => {
    const { id } = req.params
    const result = await membersBLL.deleteMember(id)
    res.json(result)
})

module.exports = router;