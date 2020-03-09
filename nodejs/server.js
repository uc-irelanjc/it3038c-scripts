var http = require("http"); 
var fs = require("fs");
var os = require("os");
var ip = require("ip");

var server = http.createServer(function(req, res){
    if(req.url === "/") {
        fs.readFile("./public/index.html","UTF-8",function(err, body){
            res.writeHead(200, {"Content-Type":"text/html"}); 
            res.end(body);
        });
    }

    else if(req.url.match("/sysinfo")){
        myHostName=os.hostname();
        upTime=process.uptime();
        memoryt=(os.totalmem()/1000000);
        memoryf=(os.freemem()/1000000);
        cpu=(os.cpus().length);
        const cpum = () => [os.cpus()[0].model];
        const osInfo = (...keys) => keys.map(key => os[key]()).join(' / ');
        homeDir = os.homedir();
        var upDays=("Days: " + Math.floor(upTime/86400));
        var upHours=("Hours " + Math.floor(upTime % 86400/3600));
        var upMin=("Minutes: " + Math.floor(((upTime % 86400) % 36000)/60));
        var upSec=("Seconds: " + Math.floor((upTime % 86400)%3600)%60);
        html=`
        <!DOCTYPE html>
        <html>
         <head> 
         <title> System Info </title>
         </head>
         <body>
         <p>Hostname: ${myHostName}</p>
         <p>IP: ${ip.address()}</p>
         <p>Server Uptime: ${upDays}, ${upHours}, ${upMin}, ${upSec}</p>
         <p>Total Memory: ${memoryt} MB</p>
         <p>Free Memory: ${memoryf} MB</p>
         <p>Model: ${cpum()}</p>
         <p>Number of CPUs: ${cpu}</p>
         <p>OS Info: ${osInfo('type', 'release', 'arch')}</p>
         <p>Home Directory: ${homeDir}</p>
         </body>
         </html>
        `
        res.writeHead(200, {"Content-Type":"text/html"});
        res.end(html);
    }

    else {
        res.writeHead(404, {"Content-Type":"text/plain"});
        res.end(`404 File Not Found at ${req.url}`); 
    }
});

server.listen(3000); 
console.log("Server listening on port 3000");