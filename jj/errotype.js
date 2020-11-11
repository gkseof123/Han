function callTenTimes(callback){
    if (callback){

    
    for (let i = 0 ; i < 10 ; i++){
        callback();
    }
} else{
    console.log("매개변수 callback이 지정되지 않았습니다.");
}

}

callTenTimes(function(){console.log("Hello")});





