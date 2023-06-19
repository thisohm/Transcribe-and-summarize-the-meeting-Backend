const express = require("express")
const router = express.Router()

const meeting = require("../controllers/about-meeting.controller")

router.post('/create', meeting.create); //create meeting

router.get('/list', meeting.get); //get meeting

router.post('/meet-id-list', meeting.getMeetById); //get meeting by meeting id

router.delete('/delete', meeting.delete) //delete meeting

module.exports = router