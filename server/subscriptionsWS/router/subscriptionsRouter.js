const express = require('express')
const router = express.Router();

const subscriptionsBLL = require("../BLL/subscriptionsBLL");

router.route('/').get(async (req, res) => {
    const subscriptions = await subscriptionsBLL.getAllSubscriptions();
    res.json(subscriptions);
});

router.route("/:id").get(async (req, res) => {
    const { id } = req.params
    const subscription = await subscriptionsBLL.getSubscriptionById(id)
    res.json(subscription)
})

router.route('/').post(async (req, res) => {
    const newSubscription = req.body
    const result = await subscriptionsBLL.addSubscription(newSubscription)
    res.json(result)
})

router.route('/:id').put(async (req, res) => {
    const { id } = req.params
    const updatedSubscription = req.body
    const result = await subscriptionsBLL.updateSubscription(id, updatedSubscription)
    res.json(result)
})

router.route('/:id').delete(async (req, res) => {
    const { id } = req.params
    const result = await subscriptionsBLL.deleteSubscription(id)
    res.json(result)
})

module.exports = router;