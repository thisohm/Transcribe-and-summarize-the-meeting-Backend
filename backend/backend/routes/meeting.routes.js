const express = require("express")
const router = express.Router()

const meeting = require("../controllers/about-meeting.controller")

router.post('/create', meeting.create); //create meeting

router.get('/list', meeting.get); //get meeting

router.get('/list-trash', meeting.getTrash); // get trash

router.post('/meet-id-list', meeting.getMeetById); //get meeting by meeting id

router.post('/move-to-trash', meeting.changeToZero); //move meeting to trash

router.post('/recover-to-meet', meeting.changeToOne); //recover meeting from trash

router.delete('/delete', meeting.delete); //delete meeting

module.exports = router