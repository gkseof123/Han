var fs = require('fs');
fs.appendFile('mynewfile1.txt', 'This is my text', function (err){
    if (err) throw err;
    console.log('Updated');
});

var fs = require('fs');
fs.writeFile('mynewfile3.txt', 'This is my text', function (err){
    if (err) throw err;
    console.log('Replaced!');
});

var fs = require('fs');
fs.unlink('mynewfile2.txt', function (err){
    if (err) throw err;
    console.log('File deleted!');
});