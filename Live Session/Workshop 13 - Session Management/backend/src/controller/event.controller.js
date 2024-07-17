const EventModel = require("../model/events.model");

exports.createEvent = async (req, res) => {
    try{
        const event = await EventModel.create(req.body);
        res.status(201).json(event);
    } catch(err){
        res.status(400).json(err);
    }
}

exports.getEvents = async (req, res) => {
    console.log(req.session)
    try{
        const events = await EventModel.find();
        res.status(200).json(events);
    } catch(err){
        res.status(400).json(err);
    }
}