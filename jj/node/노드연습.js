var http =  require('http');
var fs = require('fs')
var server = http.createServer(function(request, response){
fs.readFile("테트리스.html", function(err, data){
    response.writeHead(200,{'Content-Type':'text/html'});
    response.write(data);
    response.end();

})
});


server.listen(8000),function(){
    console.log('Server running at http://127.0.0.1:8000');
};