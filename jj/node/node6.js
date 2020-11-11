var http = require('http');
http.createServer(function(request, response){
 response.writeHead(302,{ 'Location': 'http://www.naver.com'});
 response.end();
}).listen(8000,function(){
    console.log('Server running at http://127.0.0.1:8000');
});