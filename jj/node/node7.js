var http = require('http');
var fs = require('fs');
var url = require('url');
http.createServer(function(request, response){
    var pathName = url.parse(request.url).pathname;
    if (pathName == '/'){
        fs.readFile('Index.html', function(error, data){
            response.writeHead(200,{'Content-Type':'text/html'});
            response.end(data);
        });
    } else if (pathName == '/OtherPage'){
        fs.readFile('OtherPage.html', function(error,data){
            response.writeHead(200,{'Content-Type':'text/html'});
            response.end(data);
        });
    }
}).listen(8000,function(){
    console.log('Serer running at http://127.0.0.1:8000');
});