frontend = async (app) => {
    app.get('/', function (req, res) {
        res.redirect('http://localhost:3000')
    });
};
module.exports = frontend