const mongoose = require("mongoose");
const bcrypt = require("bcrypt");
const SALT = 10;

const authSchema = mongoose.Schema({
    email: {
        type: String,
        required: true,
        unique: true,
        lowercase: true,
        trim: true,
        match: [/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/, 'Please fill a valid email address']
    },
    password: {
        type: String,
        required: true,
        minlength: 6,
        select: false
    },
    role: {
        type: String,
        enum: ["user", "admin"],
        default: "user"
    },
    isActive: {
        type: Boolean,
        default: true
    }    
});

authSchema.pre("save", function (next) {
    if (!this.isModified("password")) return next();

    bcrypt.hash(this.password, SALT, (err, hash) => {
        if (err) return next(err);
        this.password = hash;
        next();
    });
});

authSchema.methods.comparePassword = function (candidatePassword, cb) {
    bcrypt.compare(candidatePassword, this.password, (err, isMatch) => {
        if (err) return cb(err);
        cb(null, isMatch);
    });
};

module.exports = mongoose.model("Auth", authSchema);