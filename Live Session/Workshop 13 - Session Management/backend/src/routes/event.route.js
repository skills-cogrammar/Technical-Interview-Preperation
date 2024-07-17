const router = require("express").Router();
const { verifyAdmin, verifyJwt } = require("../middleware/jwt.middleware");
const { createEvent, getEvents }  = require("../controller/event.controller");

router.post("/events", verifyJwt, createEvent);
router.get("/events", getEvents);

module.exports = router;