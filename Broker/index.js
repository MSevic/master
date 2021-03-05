var express = require('express');
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);
// console.log(__dirname);
// app.use(express.static(__dirname+'/public'));
app.get('/', function (req, res) {
    res.send({'hello world': "world"})
    // res.sendfile(__dirname+'/public/registration.html');
});
io.on('connection', function (socket) {
    console.log("New Connection")
});

http.listen(8080, function () {
    console.log('listening on *:8080');
});