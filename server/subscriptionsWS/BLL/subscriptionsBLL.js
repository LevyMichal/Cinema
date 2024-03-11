const SubscriptionModel = require("../models/subscriptionModel")

//get all subscriptions
async function getAllSubscriptions() {
    const subscriptions = await SubscriptionModel.find({})
    return subscriptions
}

//get subscription by id
async function getSubscriptionById(id) {
    const subscription = await SubscriptionModel.findById(id)
    return subscription
}

// add subscription
async function addSubscription(subscriptionData) {
    const allSubscriptions = await getAllSubscriptions()

    // Find the index of the subscription with the same memberId
    const index = allSubscriptions.findIndex((s) => subscriptionData.memberId === s.memberId)

    // If the subscription doesn't exist, create a new one
    if (index === -1) {
        const newSubscription = new SubscriptionModel(subscriptionData)
        finalSubscription = await newSubscription.save()
        return finalSubscription
    } else {
        // Update the movies array of the existing subscription
        allSubscriptions[index].movies.push(...subscriptionData.movies)

        // Save the updated subscription
        const updatedSubscription = await allSubscriptions[index].save()
        return updatedSubscription
    }
}


//update subscription
async function updateSubscription(id, subscription) {
    await SubscriptionModel.findByIdAndUpdate(id, subscription)
    const updatedSubscription = getSubscriptionById(id)

    return updatedSubscription
}

//delete subscription
async function deleteSubscription(id) {
    await SubscriptionModel.findByIdAndDelete(id)
    return `the subscription with ID ${id} DELETED`
}

module.exports = { getAllSubscriptions, getSubscriptionById, addSubscription, updateSubscription, deleteSubscription }