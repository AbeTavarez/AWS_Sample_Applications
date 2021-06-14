const express = require("express")

const app = express()
const PORT = 3000

app.get('/', (req, res) => {
    res.send('Welcome to my simple WEBSERVER')
})

app.listen(PORT, () => {
    console.log(`Server listeing on port ${PORT}...`)
})