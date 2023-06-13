const db = require("../configs/config-connection");

module.exports = class agenda {

    constructor(dataInfo) {
        this.meeting_id = dataInfo?.meeting_id || ""
        this.agenda_id = dataInfo?.agenda_id || ""
        this.agentopic = dataInfo?.agentopic || ""
        this.agendetail = dataInfo?.agendetail || ""
        this.agentime = dataInfo?.agentime || ""
    }

    static create(dataInfo) {
        return db.query(`
            INSERT
            INTO    agenda
            SET     ?`,
            [dataInfo]
        )
    }

}