var fs = require('fs');
fs.appendFile('mynewfile1.txt', 'Hello content!', function (err){
    if (err) throw err;
    console.log('Saved!');
});
var fs = require('fs');
fs.appendFile('mynewfile2.txt', 'w', function (err, file){
    if (err) throw err;
    console.log('Saved!');
});
var fs = require('fs');
fs.appendFile('mynewfile3.txt', 'Hello content!', function (err){
    if (err) throw err;
    console.log('Saved!');
});