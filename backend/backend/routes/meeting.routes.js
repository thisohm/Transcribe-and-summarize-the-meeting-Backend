const express = require("express")
const router = express.Router()

const meeting = require("../controllers/about-meeting.controller")

router.route('/create').post(meeting.create); //create meeting

module.exports = router