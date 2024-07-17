const authModel = require("../model/auth.model")
const jwt = require("jsonwebtoken");
const JWT_SECRET = "supersecrettoken";

async function createUser(req, res){    
    const { email, password } = req.body;    

    try{
        const user = await authModel.create({ email, password });
        console.log(user)
        res.status(201).json(user);
    } catch(err){
        res.status(400).json(err);    
    }
}

async function authenticateUser(req, res, next){
    const {email, password} = req.body;

    const user = await authModel.findOne({email}).select('+password');

    if (!user){
        const error = new Error("User not Found")
        error.status = 403
        return next(error);
    }



    try{
        const user = await authModel.findOne({email}).select('+password');

        if (!user){
            res.status(400).json({error: "User not found"});
        }

        user.comparePassword(password, (err, isMatch) => {
            if (err) throw err;

            if (isMatch){
                const payload = {
                    id: user._id,
                    role: user.role
                }

                const token = jwt.sign(payload, JWT_SECRET, {expiresIn: "7d"});
                
                req.session.token = token;

                res.status(200).json({message: "User authenticated", token: token});
            } else{
                res.status(400).json({message: "Invalid credentials"})
            }
        });
    } catch(err){
        res.status(400).json(err);    
    }
}

module.exports = {
    createUser,
    authenticateUser
}