const Express = require("express");
const cors = require("cors");
const mongoose = require("mongoose");
const session = require("cookie-session");

const app = Express();

const expiryDate = new Date(Date.now() + 60 * 60 * 1000); // 1 hour
app.use(session({
    name: "session",
    keys: ["key1", "key2"],
    cookie: {
        secure: true,
        httpOnly: true,
        domain: "example.com",
        path: "path",
        expires: expiryDate
    }
}))

app.use(cors());
app.use(Express.json())

const MONGO_URI = process.env.MONGO_URI || "mongodb://localhost:27017";

mongoose.connect(MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true, dbName: "tipp_events" })
.then(() => console.log("Connected to database"))
.catch((err) => console.log(err));

const authRoute = require("./routes/auth.route");
const eventRoute = require("./routes/event.route");

app.use("", authRoute);
app.use("", eventRoute);

module.exports = app;