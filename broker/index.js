var express = require('express');
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var path = require('path');
var frontend = require('./sevices/forntend/service')
// console.log(__dirname);
// app.use(express.static('../Frontend'));
app.get('/', function (req, res) {
    // res.send({'hello world': "path.join(__dirname, '../Frontend', 'index.html'"})
    // res.sendFile(path.join(__dirname, '../Frontend', 'index.html'));
    frontend(res)
    // res.send(result())
    // res.send('123123');
});
io.on('connection', function (socket) {
    console.log("New Connection")
});

http.listen(8000, function () {
    console.log('listening on *:8000');
});