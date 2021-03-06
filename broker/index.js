var express = require('express');
var cors = require('cors');
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var frontend = require('./sevices/forntend/service')
var predictor = require('./sevices/predictor/service')
var md3rw = require('./sevices/modelator_d3_rw/service')
app.use(cors())
frontend(app)

md3rw(app)
app.get('/md3rw', function (req, res) {
    md3rw(res)
});
predictor(app)
io.on('connection', function (socket) {
    console.log("New Connection")
});

http.listen(8000, function () {
    console.log('listening on *:8000');
});