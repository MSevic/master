const got = require('got');

md3rw = (callback) => {

    got('http://modelator_d3_rw:6001').then(response => {
        callback.send(response.body);
    }).catch(error => {
        console.log(error.response.body);
    });
}

module.exports = md3rw