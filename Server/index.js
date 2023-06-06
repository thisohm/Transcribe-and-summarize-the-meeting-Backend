const express = require('express')
const app = express()
const mysql = require('mysql')
const cors = require('cors')

app.use(cors())
app.use(express.json())

const db = mysql.createConnection({
    user:"root",
    host:"localhost",
    database:"meeting_sum"
})

app.get('/fileinfo',(req,res) => {
    db.query("SELECT * FROM fileinfo",(err,result) =>{
        if (err){
            console.log(err)
        }else{
            res.send(result)
        }
    })
})

app.post('/create',(req,res) => {
    const meettype = req.body.meettype
    const meetapp = req.body.meetapp
    const location = req.body.location
    const topic = req.body.topic
    const datemeet = req.body.datemeet
    const timemeet = req.body.timemeet

    db.query("INSERT INTO fileinfo (meettype,meetapp,location,topic,datemeet,timemeet) VALUES(?,?,?,?,?,?)",
    [meettype,meetapp,location,topic,datemeet,timemeet],(err,result) => {
        if (err){
            console.log(err)
        }else{
            res.send("Values inserted")
        }
    }) 
})


app.listen('3001',() => {
    console.log('Server is running on port 3001')
})