const express = require('express');
const cors = require('cors');

require("./configs/subscriptionDB")

//connect to subscriptionsDB 
const app = express();
app.use(express.json());
app.use(cors());


//routers
const moviesRouter = require("./router/moviesRouter");
const membersRouter = require("./router/membersRouter");
const subscriptionsRouter = require("./router/subscriptionsRouter")

//routes
app.use('/movies', moviesRouter)
app.use('/members', membersRouter)
app.use('/subscriptions', subscriptionsRouter)



app.listen(8000, () => {
    console.log("Server listening on port 8000")
})


