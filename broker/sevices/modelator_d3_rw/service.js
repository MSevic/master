const got = require('got');
const proxy = require('express-http-proxy');


md3rw = (app) => {
    app.get('/md3rw', function (req, res) {
        got('http://modelator_d3_rw:6001').then(response => {
            res.send(response.body);
        }).catch(error => {
            res.send(error.response.body);
        });
    });


    app.use('/md3rw/rw/d3', proxy('modelator_d3_rw:6001', {
        reqBodyEncoding: null,
        preserveHostHdr: true,
        proxyReqPathResolver: function(req){
            return "/rw/d3";
        }
    }));
}

module.exports = md3rw