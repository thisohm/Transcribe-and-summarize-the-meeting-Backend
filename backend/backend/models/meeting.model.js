const db = require("../configs/config-connection");

module.exports = class meeting {

    constructor(dataInfo) {
        this.meeting_id = dataInfo?.meeting_id || ""
        this.meettype = dataInfo?.meettype || ""
        this.meetapp = dataInfo?.meetapp || ""
        this.location = dataInfo?.location || ""
        this.topic = dataInfo?.topic || ""
        this.meetdate = dataInfo?.meetdate || ""
        this.meettime = dataInfo?.meettime || ""
        this.created_timestamp = dataInfo?.created_timestamp || ""
    }
    
    static create(dataInfo) {
        return db.query(`
            INSERT
            INTO    meeting
            SET     ?`,
            [dataInfo]
        )
    }

    //get all
    static get() {
        return db.query(`
            SELECT  *
            FROM    meeting`,
        )
    }

    static getByMeetId(meeting_id) {
        return db.query(`
            SELECT  *
            FROM    meeting
            WHERE   meeting_id = ?` ,
            [meeting_id]
        )
    }

    static delete(meeting_id) {
        return db.query(`
            DELETE  
            FROM    meeting
            WHERE   meeting_id = ?` ,
            [meeting_id]
        )
    }

}