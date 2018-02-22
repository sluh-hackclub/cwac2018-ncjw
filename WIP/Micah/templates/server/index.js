var express = require('express');
//var server = require('./server.js');
var app = express();
var path    = require("path");
var bodyParser = require('body-parser');
var session = require('express-session');
// var coder = require('lib/base64-arraybuffer.js');
var mysql = require('mysql');

var con = mysql.createConnection({
  host: "160.153.33.199",
  user: "ncjw",
  password: "ncjw123!",
  database: "ncjw"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
});
var cors = require('cors')
 
app.use(cors())
app.use(express.static('public'));

app.get('/api/getData', function (req, res) {
 res.send(sessData);
})

app.get('/api/getIData/:id', function (req, res) {

	  con.query("SELECT * FROM categories where parentId="+req.params.id, function (err, result, fields) {
	    if (err) throw err;
	    res.send(result);
	  });


})
app.get('/api/getParent/:id', function (req, res) {

	  con.query("SELECT parentId FROM categories where id="+req.params.id, function (err, result, fields) {
	    if (err) throw err;
	    res.send(result);
	  });


})

app.get('/api/getPrices/:ids', function (req, res) {

	  con.query("SELECT * FROM prices where tier3='"+req.params.ids+"'", function (err, result, fields) {
	    if (err) throw err;
	    res.send(result);
	  });


})

app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(session({secret: 'ssshhhhh'}));
/**bodyParser.json(options)
 * Parses the text as JSON and exposes the resulting object on req.body.
 */
app.use(bodyParser.json());
var sessData={'empData':[]};
app.post('/api/storeData', function(req, res, next){
console.log(req.body);
var ts = Math.round((new Date()).getTime() / 1000);
sessData.empData=req.session;
sessData.empData[ts]=req.body;
//sessData.empData.push(req.body);
 res.send(req.body);
});



app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
})