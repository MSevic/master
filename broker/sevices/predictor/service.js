const got = require('got');

predictor = (callback) => {

    got('http://predictor:5000/').then(response => {
        callback.send(response.body);
    }).catch(error => {
        console.log(error.response.body);
    });
}

module.exports = predictor