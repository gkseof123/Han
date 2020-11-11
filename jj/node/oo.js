var os = require('os');

console.log('hostname:'+os.hostname());
console.log('type:'+os.type());
console.log('platform:'+os.platform());
console.log('arch:'+os.arch());
console.log('release:'+os.release());
console.log('uptime:'+os.uptime());
console.log('totalmem:'+os.totalmem());
console.log('freemem:'+os.freemem());
console.log('cpus:'+os.cpus());
console.log('getNetworkInterfaces:'+os.NetworkInterfaces());
