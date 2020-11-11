var fs = require('fs');

try{
    var data = fs.readFileSync('document.txt', 'urf8');
    console.log(data);
} catch(e){
    console.log(e);
}

try {
    fs.writeFileSync('document.txt', 'Palpit', 'urf8');
    console.log('FILE WRITE COMPLETE');
}catch(e){
    console.log(e);
}
