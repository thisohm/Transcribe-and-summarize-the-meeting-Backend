const uuid = require("uuid");

const Meeting = require("../models/meeting.model");
const Agenda = require("../models/agenda.model");

exports.create = async (req, res, next) => {
    let { meettype, meetapp, location, topic, meetdate, meettime, agendaData } = req.body
    
    try {
        const id = uuid.v4()

        let meetingInfo = new Meeting()
        meetingInfo.meeting_id = id
        meetingInfo.meettype = meettype
        meetingInfo.meetapp = meetapp
        meetingInfo.location = location
        meetingInfo.topic = topic
        meetingInfo.meetdate = meetdate
        meetingInfo.meettime = meettime
        meetingInfo.created_timestamp = new Date(Date.now())
        await Meeting.create(meetingInfo);
        
        for(let agenlist of agendaData){
            let agendaInfo = new Agenda()
            agendaInfo.meeting_id = id
            agendaInfo.agenda_id = uuid.v4()
            agendaInfo.agentopic = agenlist.agentopic
            agendaInfo.agendetail = agenlist.agendetail
            agendaInfo.agentime = agenlist.agentime
            await Agenda.create(agendaInfo);
        }
        
        res.status(200).json({
            message:"Meeting create success",
            "meet_id": meetingInfo.meeting_id,
        })
    }
    catch (error) {
        if(!error.statusCode) {
            error.error = error
            error.statusCode = 500;
            error.message = "Meeting create failed";
        }
        next(error);
    }
    
}

exports.get = async (req, res, next) => {

    try{
        let [userInfo] = await Meeting.get();
        res.status(200).json({ 
            message:"Meeting get success",
            result: userInfo
        })
    }
    catch (error) {
        if(!error.statusCode) {
            error.error = error
            error.statusCode = 500;
            error.message = "Meeting get failed";
        }
        next(error);
    }
}

exports.getMeetById = async (req, res, next) => {
    let {meeting_id} = req.body

    try{
        let [userInfo1] = await Meeting.getByMeetId(meeting_id);
        let [userInfo2] = await Agenda.getByMeetId(meeting_id);
        res.status(200).json({
            message:"Meeting and Agenda get by meeting_id success",
            meeting: userInfo1,
            agenda: userInfo2
        })
    }
    catch (error) {
        if(!error.statusCode) {
            error.error = error
            error.statusCode = 500;
            error.message = "Meeting get by meeting_id failed";
        }
        next(error);
    }
}

exports.delete = async (req, res, next) => {
    let {meeting_id} = req.body

    try{
        await Meeting.delete(meeting_id);
        res.status(200).json({
            message:"Meeting delete success",
            
        })
    }
    catch (error) {
        if(!error.statusCode) {
            error.error = error
            error.statusCode = 500;
            error.message = "Meeting delete failed";
        }
        next(error);

    }
}

