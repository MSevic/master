var express = require('express');
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var frontend = require('./sevices/forntend/service')
var predictor = require('./sevices/predictor/service')
var md3rw = require('./sevices/modelator_d3_rw/service')
// console.log(__dirname);
// app.use(express.static('../Frontend'));
app.get('/', function (req, res) {
    frontend(res); // res.sendFile(path.join(__dirname, '../Frontend', 'index.html'));
});
app.get('/md3rw', function (req, res) {
    md3rw(res)
});
app.get('/predictor', function (req, res) {
    predictor(res)
});
io.on('connection', function (socket) {
    console.log("New Connection")
});

http.listen(8000, function () {
    console.log('listening on *:8000');
});