var http = require('http');
var fs = require('fs');

var url = "127.0.0.1";
var port = 3000;

var app = http.createServer(function(request,response){
    var url = request.url; //기본 url http://127.0.0.1에 할당
    if(request.url == '/'){
      url = '/test.html';
    }
    if(request.url == '/favicon.ico'){
        response.writeHead(404);
        response.end();
        return;
      }
    response.writeHead(200);
    response.end(fs.readFileSync(__dirname + url));
});
app.listen(port);
console.log('Server running at http://'+ url +':' + port);