const got = require('got');

predictor = (app) => {
    app.get('/predictor', function (req, res) {
        got('http://predictor:5000/').then(response => {
            res.send(response.body);
        }).catch(error => {
            console.log(error.response.body);
        });
    });

    app.get('/predictor/predictions/:commodity?/:count?', (req, res) => {
        var url = 'http://predictor:5000/predictions/';
        if( req.params.commodity){
            var count = req.params.count || 0;
            url += req.params.commodity + "/" +count
        }
        got(url).then(response => {
            res.send(response.body);
        }).catch(error => {
            res.send(error.response.body);
        });


    })
}

module.exports = predictor