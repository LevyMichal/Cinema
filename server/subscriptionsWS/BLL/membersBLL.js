const MemberModel = require("../models/memberModel")


//get all members
async function getAllMembers() {
    const members = await MemberModel.find({})
    return members
}

//get member by id
async function getMemberById(id) {
    const member = await MemberModel.findById(id)
    return member
}

//add member
async function addMember(member) {
    const newMember = new MemberModel(member)
    await newMember.save()
    return newMember
}

//update member
async function updateMember(id, member) {
    await MemberModel.findByIdAndUpdate(id, member)
    updatedMember = getMemberById(id)
    return updatedMember
}

//delete member
async function deleteMember(id) {
    await MemberModel.findByIdAndDelete(id)
    return `the member with ID ${id} DELETED`
}

module.exports = { getAllMembers, getMemberById, addMember, updateMember, deleteMember }