const uuid = require("uuid");

const Meeting = require("../models/meeting.model");
const Agenda = require("../models/agenda.model");

exports.create = async (req, res, next) => {
    let { meettype, meetapp, location, topic, meetdate, meettime, agendaData } = req.body
    
    try {
        
        let meetingInfo = new Meeting()
        meetingInfo.meeting_id = uuid.v4()
        meetingInfo.meettype = meettype
        meetingInfo.meetapp = meetapp
        meetingInfo.location = location
        meetingInfo.topic = topic
        meetingInfo.meetdate = meetdate
        meetingInfo.meettime = meettime
        await Meeting.create(meetingInfo);
        
        for(let agenlist of agendaData){
            let agendaInfo = new Agenda()
            agendaInfo.meeting_id = meetingInfo.meeting_id
            agendaInfo.agenda_id = uuid.v4()
            agendaInfo.agentopic = agenlist.agentopic
            agendaInfo.agendetail = agenlist.agendetail
            agendaInfo.agentime = agenlist.agentime
            await Agenda.create(agendaInfo);
        }   
        
        res.status(200).json({
            message:"Meeting create success"
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