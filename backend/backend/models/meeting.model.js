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
    }

    static create(dataInfo) {
        return db.query(`
            INSERT
            INTO    meeting
            SET     ?`,
            [dataInfo]
        )
    }

    //agenda

}