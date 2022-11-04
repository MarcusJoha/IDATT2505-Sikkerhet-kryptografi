const express = require('express');
const path = require('path');

const app = express();
app.use(express.static('../static'));

const port = process.env.PORT || 8080;

// sendFile will go here
app.get("/", function(req, res) {
    res.sendFile(path.join(__dirname, "../static/"))
})

app.listen(port);
console.log('Server started at http://localhost:' + port);