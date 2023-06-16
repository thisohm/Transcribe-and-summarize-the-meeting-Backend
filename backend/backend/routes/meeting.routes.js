const express = require("express")
const router = express.Router()

const meeting = require("../controllers/about-meeting.controller")

router.route('/create').post(meeting.create); //create meeting
router.route('/list').get(meeting.get); //get meeting
router.route('/delete').delete(meeting.delete) //delete meeting

module.exports = router