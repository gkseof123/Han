

public class DataTypeEx5 { 
            public  static void main(String[] args ){ 
              //long 타입은 정수타비, 8byte할당, -2147483648~2147483641범위를 넘는 //정수는 반드시 L 또는 l 을 함께 정수값에 선언해야합니다.
            long num = 1 ; //num = 1L;
          //  num = 2147483648; error
              num = 2147483648L;
              System.out.println(num);
            //  int num2 = 0.5;
              //  num = 0.5;
          //flaot타입은 실수타입, 4byte할당, 지수부와 가수부로 부동소수점 형식을 저장됨
         //   float f = 0.5;  //0.5는 JVM이 8byte부동소수점형식으로 만듬
              float f = 0.5F;  //f=0.5f;
      //double타읍은 실수타입, 8byte할당, 지수부와 가수부로 부동소수점 형식을 저장됨
             double d = 0.5;
              System.out.println(f);          
              System.out.println(d);    
             d = 1.5D; // d= 1.5d;
              System.out.println(d);       
         //2147483648 값을 IEEE표기형식 2.124783648E9
               d =  2.124783648E9;
             double  d2 =  2124783648L;
              System.out.println(d);
              System.out.println((long)d==(long)d2);
              
}           
}