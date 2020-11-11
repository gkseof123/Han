

public class DataTypeEx4 { 
            public  static void main(String[] args ){ 
            //int는 4byte 할당, -2^31~2^31-1, -2147483678~2147483647
              int num = 2147483647 ;
              num = (int)2147483648L;
               long num2 = 2147483648L;  //long은 8byte로 할당
              System.out.println(num);
              System.out.println(num2);
              num = 011;
              System.out.println(num);
              num = 077;
              System.out.println(num);
              num = 0x77;    //16진수
              System.out.println(num);
              num = 0xff;
              System.out.println(num);
              num = 'A';
              System.out.println(num);
}           
}