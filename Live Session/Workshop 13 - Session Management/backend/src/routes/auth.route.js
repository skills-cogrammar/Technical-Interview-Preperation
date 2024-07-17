const router = require("express").Router();
const { authenticateUser, createUser } = require("../controller/auth.controller")

router.post("/sign-up", createUser);
router.post("/login", authenticateUser);

module.exports = router;