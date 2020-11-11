

public class CastEx { 
            public  static void main(String[] args ){ 
          int num = 4 ; 
         double d = num; //promotion
        // int num2 = d;
//큰타입을 작은타입에 할당할때 자동 형변환이 일어나지 않되므로 , 명시적인 //형변환casting을 해야합니다.
       int num2 = (int) d;
          byte b1 = 65;
          char ch = (char)b1;
          num2 = 0;
          boolean b2 = (boolean)num2;
}           
}