/*
try{
    const array = new Array(-2000);  
} catch (exception){
    console.log(`${exception.name}예외가 발생했습니다.`);
   
} finally{
    console.log("finally 구문이 실행되었습니다.");
}

const error = new Error('메시지');

error.name = '바람이 직방으로 와서 사망';

error.message = '사망';


throw error;
*/
try {
    throw '예외가 발생했습니다.';
} catch ( exception){
    console.log('예외가 발생했습니다.');
    console.log(exception);
}


try {
    const error = new Error('고양이');
    error.name = '사료먹는다';
    error.message = '맛있게 먹는다';

    throw error;
} catch  (exception) {
    console.log(`${exception.name}예외가 발생했습니다.`);
    console.log(exception.message);
}