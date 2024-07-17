const jwt = require("jsonwebtoken")
const JWT_SECRET = "supersecrettoken";

function verifyJwt(req, res, next){
    const auth = req.headers.authorization;
    // const auth = req.session.token;

    if (auth){
        const token = auth.split(" ")[1];
        // const token = auth

        jwt.verify(token, JWT_SECRET, (err, user) => {            
            if (err) return res.sendStatus(403);
            req.user = user;

            next();
        });
    } else{
        res.sendStatus(401);
    }
}

function verifyAdmin(req, res, next){

    if (!req.user){
        return res.sendStatus(403);
    }

    if (req.user.role == "admin"){
        next();    
    }
    else{
        res.sendStatus(403);
    }
}

module.exports = {verifyJwt, verifyAdmin};